#!/usr/bin/env python3
"""Score third-party x402 cleaners without Dune or Codex.

Does not produce a single accuracy percentage. See docs/cleaner-audit.md.
"""

from __future__ import annotations

import gzip
import io
import json
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from httpjson import get_json, get_bytes

AGENT_JSON = "https://agenteconomy.to/data.json"
X402WATCH_RAW = (
    "https://raw.githubusercontent.com/printmoneylab/x402watch-data/main/data"
)

# Published forensic snapshots — scale checks, not live GMV.
VISA_KEEP_USD = 15_000_000 / 135_700_000  # ~Apr 2026 Visa×Artemis
PAPER_NAMED_FLOOR = 187_861 / 44_121_384  # Ling et al. Base 280d
PAPER_C3_CEILING = 20_258_746 / 44_121_384

CAMPAIGN_DATES = {
    "jul_end": "2026-07-31",
    "aug_peak": "2026-08-26",
    "aug_end": "2026-08-31",
}

PLACEHOLDER_CATS = {"premium_placeholder", "other", "unknown", "uncategorized", ""}


def month_ticket(row: dict[str, Any]) -> float | None:
    txs = row.get("txs") or 0
    vol = row.get("vol")
    if not txs or vol is None:
        return None
    return vol / txs


def load_buyer_labels(day: str) -> dict[str, Any] | None:
    try:
        return get_json(f"{X402WATCH_RAW}/buyer-labels-{day}.json")
    except Exception:
        return None


def f1_pack(blob: dict[str, Any] | None) -> dict[str, Any] | None:
    if not blob:
        return None
    rv = blob.get("real_vs_wash_30d") or {}
    labs = {x["label"]: x.get("n_buyers") or 0 for x in blob.get("label_distribution") or []}
    n = sum(labs.values()) or 1
    tot = rv.get("total_volume_usdc") or 0
    real = rv.get("real_volume_usdc") or 0
    wash = rv.get("wash_volume_usdc") or 0
    return {
        "real": real,
        "wash": wash,
        "dev": rv.get("developer_volume_usdc") or 0,
        "total": tot,
        "keep": (real / tot) if tot else None,
        "organic_share": labs.get("organic_user", 0) / n,
        "n_buyers": n,
        "wash_buyers": labs.get("suspected_wash", 0),
    }


def check(
    checks: list[dict[str, Any]],
    cid: str,
    source: str,
    status: str,
    detail: str,
) -> None:
    checks.append({"id": cid, "source": source, "status": status, "detail": detail})


def liveness_sample(n: int = 8) -> dict[str, Any]:
    today = datetime.now(timezone.utc).date()
    services = None
    used = None
    for i in range(0, 3):
        d = today.fromordinal(today.toordinal() - i)
        url = f"{X402WATCH_RAW}/services-{d.isoformat()}.json.gz"
        try:
            raw = get_bytes(url)
        except Exception:
            continue
        if not raw or raw[:2] != b"\x1f\x8b":
            continue
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as gz:
            services = json.loads(gz.read().decode("utf-8")).get("services") or []
        used = d.isoformat()
        break
    if not services:
        return {"ok": False, "reason": "no services dump"}

    snap = date.fromisoformat(used)
    cutoff = (snap - timedelta(days=6)).isoformat()
    candidates = []
    for s in services:
        url = s.get("resource_url") or ""
        if not url.startswith("http"):
            continue
        if s.get("category") in PLACEHOLDER_CATS:
            continue
        last = str(s.get("last_seen") or "")[:10]
        if last < cutoff:
            continue
        candidates.append(s)
        if len(candidates) >= n * 8:
            break

    seen_cat: set[str] = set()
    diverse: list[dict[str, Any]] = []
    rest: list[dict[str, Any]] = []
    for s in candidates:
        cat = str(s.get("category") or "")
        if cat not in seen_cat:
            seen_cat.add(cat)
            diverse.append(s)
        else:
            rest.append(s)
    picked = (diverse + rest)[:n]
    live = 0
    dead = 0
    results = []
    for s in picked:
        url = s["resource_url"]
        status_code: int | str | None = None
        try:
            req = urllib.request.Request(
                url,
                method="HEAD",
                headers={"User-Agent": "agent-economy-monitor-audit/1.0"},
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                status_code = resp.status
        except urllib.error.HTTPError as e:
            status_code = e.code
        except Exception:
            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "agent-economy-monitor-audit/1.0"},
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    status_code = resp.status
            except urllib.error.HTTPError as e:
                status_code = e.code
            except Exception as e:
                status_code = type(e).__name__
        ok = isinstance(status_code, int) and (
            200 <= status_code < 400 or status_code == 402
        )
        if ok:
            live += 1
        else:
            dead += 1
        results.append(
            {
                "name": s.get("name"),
                "category": s.get("category"),
                "url": url,
                "status": status_code,
            }
        )
    return {
        "ok": True,
        "snapshot": used,
        "sampled": len(picked),
        "live": live,
        "dead": dead,
        "rows": results,
    }


def main() -> int:
    agent = get_json(AGENT_JSON)
    x402 = agent.get("x402") or {}
    monthly = {m.get("month"): m for m in x402.get("monthly") or []}
    jul = monthly.get("Jul 26") or {}
    aug = monthly.get("Aug 26") or {}
    mpp = agent.get("tempoMpp") or {}
    by_type = mpp.get("byType") or {}
    events = mpp.get("totalEvents") or 0
    settled = by_type.get("Settled") or 0
    token_split = x402.get("tokenSplit") or {}
    cats = None
    today = datetime.now(timezone.utc).date()
    snap_day = None
    for i in range(0, 4):
        d = date.fromordinal(today.toordinal() - i).isoformat()
        try:
            cats = get_json(f"{X402WATCH_RAW}/category-benchmarks-{d}.json")
            snap_day = d
            break
        except Exception:
            continue

    checks: list[dict[str, Any]] = []

    # A. MPP units
    ratio = (settled / events) if events else None
    if ratio is not None and ratio < 0.05 and "Settled" in by_type:
        check(
            checks,
            "A_mpp_units",
            "agenteconomy",
            "pass",
            f"Settled={settled} / events={events} ({ratio:.2%}). Feed exposes the right unit.",
        )
    else:
        check(
            checks,
            "A_mpp_units",
            "agenteconomy",
            "fail",
            f"Cannot separate Settled from events (Settled={settled}, events={events}).",
        )

    # A2. T0 campaign is visible (good for a raw feed)
    jul_txs, aug_txs = jul.get("txs") or 0, aug.get("txs") or 0
    jul_t, aug_t = month_ticket(jul), month_ticket(aug)
    if jul_txs and aug_txs / jul_txs >= 2 and aug_t and jul_t and aug_t < jul_t:
        check(
            checks,
            "A_t0_shows_campaign",
            "agenteconomy",
            "pass",
            f"Aug/Jul txs={aug_txs/jul_txs:.1f}×, ticket ${jul_t:.4f}→${aug_t:.4f}. T0 correctly looks like junk.",
        )
    else:
        check(
            checks,
            "A_t0_shows_campaign",
            "agenteconomy",
            "warn",
            "August campaign pattern not visible in monthly T0; feed may have changed.",
        )

    # B. Universe mismatch
    sample_n = token_split.get("totalPayments")
    note = token_split.get("note") or ""
    if sample_n and aug_txs and sample_n < 0.01 * aug_txs:
        check(
            checks,
            "B_usdc_share_scope",
            "agenteconomy",
            "fail",
            (
                f"tokenSplit.totalPayments={sample_n} vs Aug T0 txs={aug_txs}. "
                f"USDC share {token_split.get('usdcSharePct')}% is a restricted sample. note={note!r}"
            ),
        )
    else:
        check(
            checks,
            "B_usdc_share_scope",
            "agenteconomy",
            "info",
            f"tokenSplit n={sample_n} usdc={token_split.get('usdcSharePct')} note={note!r}",
        )

    # C. x402watch campaign backtest
    jul_f = f1_pack(load_buyer_labels(CAMPAIGN_DATES["jul_end"]))
    peak_f = f1_pack(load_buyer_labels(CAMPAIGN_DATES["aug_peak"]))
    end_f = f1_pack(load_buyer_labels(CAMPAIGN_DATES["aug_end"]))
    if jul_f and peak_f and jul_txs:
        real_ratio = peak_f["real"] / jul_f["real"] if jul_f["real"] else None
        tx_ratio = aug_txs / jul_txs
        if real_ratio is not None and real_ratio < 1.2 and tx_ratio >= 2:
            check(
                checks,
                "C_campaign_real_vs_t0_txs",
                "x402watch",
                "pass",
                (
                    f"T0 txs {tx_ratio:.1f}× but 30d real USD {real_ratio:.2f}× "
                    f"(${jul_f['real']:.0f}→${peak_f['real']:.0f} at {CAMPAIGN_DATES['aug_peak']}). "
                    "Did not follow tx Goodhart at the peak."
                ),
            )
        else:
            check(
                checks,
                "C_campaign_real_vs_t0_txs",
                "x402watch",
                "fail",
                f"30d real USD moved with T0 txs (real {real_ratio}, txs {tx_ratio:.1f}×).",
            )

    if jul_f and peak_f and end_f:
        wash_drop = peak_f["wash"] > 0 and end_f["wash"] < 0.1 * peak_f["wash"]
        real_jump = end_f["real"] > 1.4 * peak_f["real"]
        if wash_drop and real_jump:
            check(
                checks,
                "C_label_stability",
                "x402watch",
                "fail",
                (
                    f"Wash USD ${peak_f['wash']:.0f}→${end_f['wash']:.0f} while real "
                    f"${peak_f['real']:.0f}→${end_f['real']:.0f} in five days. "
                    "Reclassification, not a market."
                ),
            )
        else:
            check(
                checks,
                "C_label_stability",
                "x402watch",
                "pass",
                "No wash-collapse + real-jump between peak and month-end.",
            )

    # D. tightness
    latest_f = end_f or peak_f or jul_f
    if latest_f and latest_f["keep"] is not None:
        keep = latest_f["keep"]
        if keep > 0.70:
            check(
                checks,
                "D_tightness_vs_forensics",
                "x402watch",
                "fail",
                (
                    f"F1 keep-rate {keep:.1%} vs Visa×Artemis ~{VISA_KEEP_USD:.0%} "
                    f"and named-floor ~{PAPER_NAMED_FLOOR:.2%}. Too loose for 表 0."
                ),
            )
        elif keep > PAPER_C3_CEILING:
            check(
                checks,
                "D_tightness_vs_forensics",
                "x402watch",
                "warn",
                f"Keep-rate {keep:.1%} is above paper C3 ceiling ~{PAPER_C3_CEILING:.0%}.",
            )
        else:
            check(
                checks,
                "D_tightness_vs_forensics",
                "x402watch",
                "pass",
                f"Keep-rate {keep:.1%} is inside forensic range.",
            )

    # E. residual buyers
    if latest_f and latest_f["organic_share"] >= 0.90:
        check(
            checks,
            "E_organic_user_residual",
            "x402watch",
            "fail",
            (
                f"organic_user is {latest_f['organic_share']:.1%} of {latest_f['n_buyers']} "
                "labeled buyers. Not Unique Buyers."
            ),
        )
    elif latest_f:
        check(
            checks,
            "E_organic_user_residual",
            "x402watch",
            "pass",
            f"organic_user share {latest_f['organic_share']:.1%}.",
        )

    # F. SKU concentration (24h)
    sku_top = None
    if cats:
        rows = (cats.get("latest_hourly_snapshot_24h") or {}).get("rows") or []
        vol = sum(r.get("total_volume_24h") or 0 for r in rows)
        if rows and vol:
            top = max(rows, key=lambda r: r.get("total_volume_24h") or 0)
            share = (top.get("total_volume_24h") or 0) / vol
            sku_top = (top.get("category"), share, vol)
            if share >= 0.50:
                check(
                    checks,
                    "F_sku_concentration",
                    "x402watch",
                    "warn",
                    f"24h SKU USD {share:.0%} in {top.get('category')} (${vol:.0f} total). Mix is a cluster, not PMF.",
                )
            else:
                check(
                    checks,
                    "F_sku_concentration",
                    "x402watch",
                    "pass",
                    f"24h top category {share:.0%} of ${vol:.0f}.",
                )

    live = liveness_sample()
    if live.get("ok") and live.get("sampled"):
        rate = live["live"] / live["sampled"]
        st = "pass" if rate >= 0.5 else "warn"
        check(
            checks,
            "F_catalog_liveness",
            "x402watch",
            st,
            f"{live['live']}/{live['sampled']} sampled named URLs responded (incl. HTTP 402 as live).",
        )
    else:
        check(
            checks,
            "F_catalog_liveness",
            "x402watch",
            "info",
            live.get("reason") or "skipped",
        )

    # Freshness
    executed = ((agent.get("meta") or {}).get("queries") or {}).get("x402Daily") or {}
    check(
        checks,
        "A_feed_freshness",
        "agenteconomy",
        "info",
        f"x402Daily executedAt={executed.get('executedAt')} credits={executed.get('lastCostCredits')} (do not re-run queryId {executed.get('queryId')}).",
    )

    fail = sum(1 for c in checks if c["status"] == "fail")
    warn = sum(1 for c in checks if c["status"] == "warn")
    out = {
        "date": date.today().isoformat(),
        "as_of": agent.get("updatedAt"),
        "x402watch_snapshot": snap_day,
        "dune_queries_this_run": 0,
        "codex_calls_this_run": 0,
        "summary": {
            "fail": fail,
            "warn": warn,
            "pass": sum(1 for c in checks if c["status"] == "pass"),
            "verdict": (
                "Do not use x402watch real USD or agenteconomy T0 as Service Spend. "
                "Use T0 as tripwire, Settled as MPP unit, 24h SKU as a mix slice only."
                if fail
                else "No hard fails; still not T3."
            ),
        },
        "benchmarks": {
            "visa_artemis_keep_usd": VISA_KEEP_USD,
            "paper_named_floor_keep_usd": PAPER_NAMED_FLOOR,
            "paper_c3_ceiling_keep_usd": PAPER_C3_CEILING,
        },
        "f1": {
            "jul_31": jul_f,
            "aug_26": peak_f,
            "aug_31": end_f,
        },
        "sku_top_24h": sku_top,
        "catalog_liveness": {k: live[k] for k in live if k != "rows"},
        "liveness_rows": live.get("rows"),
        "checks": checks,
    }
    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    print("=== CLEANER AUDIT (free, not T3) ===", file=sys.stderr)
    print(
        f"fail={fail} warn={warn}  dune=0 codex=0  {out['summary']['verdict']}",
        file=sys.stderr,
    )
    for c in checks:
        print(f"[{c['status'].upper():4}] {c['id']}: {c['detail']}", file=sys.stderr)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
