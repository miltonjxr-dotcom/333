#!/usr/bin/env python3
"""Free-desk quality panel (no Allium, no Dune, no Codex).

Reads:
  - https://agenteconomy.to/data.json          (T0 + MPP + ACP)
  - GitHub printmoneylab/x402watch-data         (CC0 catalog / 24h SKU / 30d real)

Emits JSON on stdout. GREEN is forbidden. T3/T4 fields stay null.
See docs/data-cleaning.md and config/quota.yaml.
"""

from __future__ import annotations

import gzip
import io
import json
import subprocess
import sys
import urllib.error
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from httpjson import get_bytes, get_json

AGENT_JSON = "https://agenteconomy.to/data.json"
X402WATCH_RAW = (
    "https://raw.githubusercontent.com/printmoneylab/x402watch-data/main/data"
)

PLACEHOLDER_CATS = {"premium_placeholder", "other", "unknown", "uncategorized", ""}
ACP_NEEDLES = ("virtuals.io", "acp-x402")

SKU_ROLLUP = {
    "ai_inference": "inference",
    "ai_search": "inference",
    "search_engine": "data",
    "scientific_data": "data",
    "financial_data": "data",
    "wallet_analytics": "data",
    "token_data": "data",
    "nft_data": "data",
    "weather": "data",
    "maps_location": "data",
    "business_intelligence": "data",
    "blockchain_infra": "other_api",
    "trading_signals": "other_api",
}


def load_x402watch_json(name: str, day: date) -> dict[str, Any] | None:
    """name is 'buyer-labels' or 'category-benchmarks' (plain json)."""
    url = f"{X402WATCH_RAW}/{name}-{day.isoformat()}.json"
    try:
        return get_json(url)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    except subprocess.CalledProcessError:
        return None


def load_x402watch_services(day: date) -> dict[str, Any] | None:
    url = f"{X402WATCH_RAW}/services-{day.isoformat()}.json.gz"
    try:
        raw = get_bytes(url)
    except (urllib.error.HTTPError, subprocess.CalledProcessError):
        return None
    if not raw or raw[:2] != b"\x1f\x8b":
        return None
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as gz:
        return json.loads(gz.read().decode("utf-8"))


def resolve_snapshot_day() -> date:
    """UTC today may not be published yet (dump is ~04:00 UTC). Walk back 3 days."""
    today = datetime.now(timezone.utc).date()
    for i in range(0, 4):
        d = today - timedelta(days=i)
        if load_x402watch_json("buyer-labels", d) is not None:
            return d
    raise RuntimeError("x402watch-data buyer-labels not found for last 4 UTC days")


def is_acp_service(svc: dict[str, Any]) -> bool:
    blob = " ".join(
        str(svc.get(k) or "")
        for k in ("resource_url", "name", "seller_address")
    ).lower()
    return any(n in blob for n in ACP_NEEDLES)


def sku_bucket(category: str) -> str:
    return SKU_ROLLUP.get(category, "unknown" if category in PLACEHOLDER_CATS else "other_api")


def avg_ticket(month: dict[str, Any]) -> float | None:
    txs = month.get("txs") or 0
    vol = month.get("vol")
    if not txs or vol is None:
        return None
    return vol / txs


def pick_latest_complete_day(daily: list[dict[str, Any]]) -> dict[str, Any]:
    """Skip a stub UTC-today row that would look like a crash."""
    latest_day = daily[-1] if daily else {}
    today = date.today().isoformat()
    if (
        len(daily) >= 2
        and latest_day.get("day") == today
        and (latest_day.get("txs") or 0) < 0.2 * (daily[-2].get("txs") or 1)
    ):
        return daily[-2]
    return latest_day


def sku_from_category_benchmarks(cats: dict[str, Any]) -> tuple[list[dict[str, Any]], float, int, dict[str, float]]:
    rows = (cats.get("latest_hourly_snapshot_24h") or {}).get("rows") or []
    sku_24h = [
        {
            "category": r.get("category"),
            "bucket": sku_bucket(str(r.get("category") or "")),
            "txs": r.get("total_tx_24h") or 0,
            "usd": r.get("total_volume_24h") or 0,
        }
        for r in rows
    ]
    sku_24h.sort(key=lambda r: r["usd"], reverse=True)
    f_sku_usd = float(sum(r["usd"] for r in sku_24h))
    f_sku_txs = int(sum(r["txs"] for r in sku_24h))
    rollup: dict[str, float] = {}
    for r in sku_24h:
        rollup[r["bucket"]] = rollup.get(r["bucket"], 0.0) + float(r["usd"])
    return sku_24h, f_sku_usd, f_sku_txs, rollup


def catalog_seller_counts(services: dict[str, Any] | None, snap_day: date) -> tuple[int | None, int | None, int | None]:
    if not services or not services.get("services"):
        return None, None, None
    cutoff = (snap_day - timedelta(days=6)).isoformat()
    live = 0
    named = 0
    acp = 0
    for svc in services["services"]:
        if is_acp_service(svc):
            acp += 1
            continue
        last_seen = str(svc.get("last_seen") or "")
        if last_seen[:10] < cutoff:
            continue
        live += 1
        cat = svc.get("category") or ""
        if cat not in PLACEHOLDER_CATS:
            named += 1
    return live, named, acp


def build_panel() -> dict[str, Any]:
    agent = get_json(AGENT_JSON)
    snap_day = resolve_snapshot_day()
    buyer = load_x402watch_json("buyer-labels", snap_day)
    cats = load_x402watch_json("category-benchmarks", snap_day)
    services = load_x402watch_services(snap_day)
    if buyer is None or cats is None:
        raise RuntimeError(f"incomplete x402watch snapshot for {snap_day}")

    x402 = agent.get("x402") or {}
    daily = x402.get("daily") or []
    monthly = x402.get("monthly") or []
    latest_day = pick_latest_complete_day(daily)
    last_month = monthly[-1] if monthly else {}

    sku_24h, f_sku_usd, f_sku_txs, rollup = sku_from_category_benchmarks(cats)

    rv = buyer.get("real_vs_wash_30d") or {}
    labels = {row["label"]: row.get("n_buyers") for row in buyer.get("label_distribution") or []}
    live_sellers, live_named, acp_catalog_rows = catalog_seller_counts(services, snap_day)

    mpp = agent.get("tempoMpp") or {}
    acp_feed = agent.get("virtualsAcp") or {}
    acp_daily = acp_feed.get("daily") or []
    token_split = x402.get("tokenSplit") or {}

    snapshot = {
        "date": date.today().isoformat(),
        "as_of": agent.get("updatedAt")
        or datetime.now(timezone.utc).isoformat(),
        "quality_available": False,
        "quality_note": (
            "Free desk: Observed Service Spend is null. T3/T4 are null. "
            "Do not treat F_sku USD, F1 30d real, T0, or MPP Settled counts "
            "as Service Spend. Do not add USD to transaction counts. "
            "GREEN is forbidden."
        ),
        "observed_service_spend_usd": None,
        "x402": {
            "t0_txs": latest_day.get("txs"),
            "t0_usd": latest_day.get("vol"),
            "t2_usd": None,
            "t3_usd": None,
            "t4_usd": None,
            "t3_payers": None,
            "t3_payees": None,
            "t2_avg_ticket": avg_ticket(last_month),
            "top1pct_buyer_share": None,
            "usdc_share": token_split.get("usdcSharePct"),
            "chain_t2_usd_share": None,
        },
        "free_proxy": {
            "x402watch_snapshot_date": snap_day.isoformat(),
            "f1_real_volume_30d_usd": rv.get("real_volume_usdc"),
            "f1_total_volume_30d_usd": rv.get("total_volume_usdc"),
            "f1_wash_volume_30d_usd": rv.get("wash_volume_usdc"),
            "f1_developer_volume_30d_usd": rv.get("developer_volume_usdc"),
            "f_sku_usd_24h": f_sku_usd,
            "x402_covered_sku_spend_proxy_usd": f_sku_usd,
            "f_sku_txs_24h": f_sku_txs,
            "f_sku_24h_by_category": sku_24h[:15],
            "f_sku_24h_rollup": rollup,
            "live_sellers_7d": live_sellers,
            "live_named_sellers_7d": live_named,
            "acp_catalog_rows_excluded": acp_catalog_rows,
            "buyer_label_counts": labels,
            "unique_buyers": None,
            "repeat_buyer_rate": None,
            "note": (
                "F1 is x402watch 'real' (crawlers still in, ACP not stripped). "
                "organic_user count is a residual class, not Unique Buyers. "
                "24h SKU USD is a covered-SKU proxy, not x402 Service Spend."
            ),
        },
        "tempo_mpp": {
            "settled": (mpp.get("byType") or {}).get("Settled"),
            "settled_paid_events": (mpp.get("byType") or {}).get("Settled"),
            "settled_usd": None,
            "channel_opened": (mpp.get("byType") or {}).get("ChannelOpened"),
            "unique_payers": mpp.get("uniquePayers"),
            "unique_payees": mpp.get("uniquePayees"),
        },
        "virtuals_acp": {
            "memos": acp_feed.get("totalMemos"),
            "unique_senders": (acp_daily[-1] or {}).get("senders") if acp_daily else None,
        },
        "erc8004": {
            "registrations": (agent.get("erc8004Registry") or {}).get("totalAgents"),
            "reputation_with_payment_proof": None,
        },
        "openrouter": {
            "cli_agent_tokens": None,
            "reasoning_share": None,
            "note": "Weekly eyeball only. No daily Data API (config/quota.yaml).",
        },
        "public_tripwire": {
            "x402_daily_txs": float(latest_day.get("txs") or 0),
            "x402_month_avg_ticket": avg_ticket(last_month),
            "x402_month": last_month.get("month"),
            "x402_month_txs": last_month.get("txs"),
            "x402_month_vol": last_month.get("vol"),
            "source": AGENT_JSON,
            "note": "T0-like public aggregates. GREEN is forbidden from this desk.",
        },
        "alerts": [],
        "quota": {
            "dune_queries_this_run": 0,
            "codex_calls_this_run": 0,
        },
    }

    # Concentration in 24h SKU is a yellow hint, not green.
    if f_sku_usd > 0 and sku_24h:
        top_share = sku_24h[0]["usd"] / f_sku_usd
        if top_share >= 0.50:
            snapshot["alerts"].append(
                {
                    "id": "F_sku_concentrated",
                    "level": "yellow",
                    "reason": (
                        f"24h SKU USD {top_share:.0%} in {sku_24h[0]['category']} "
                        f"(${sku_24h[0]['usd']:.2f} of ${f_sku_usd:.2f}). "
                        "Cluster/campaign until a Dune sample says otherwise."
                    ),
                }
            )

    return snapshot


def main() -> int:
    snapshot = build_panel()
    json.dump(snapshot, sys.stdout, indent=2)
    sys.stdout.write("\n")

    proxy = snapshot["free_proxy"]
    print("=== FREE DESK PANEL (T3/T4 unavailable) ===", file=sys.stderr)
    print(
        f"Observed Spend=null  x402watch={proxy.get('x402watch_snapshot_date')}  "
        f"covered_SKU_proxy=${proxy.get('f_sku_usd_24h'):.2f} txs={proxy.get('f_sku_txs_24h')}  "
        f"live_named_sellers_7d={proxy.get('live_named_sellers_7d')}",
        file=sys.stderr,
    )
    print(
        f"T0 day txs={snapshot['x402'].get('t0_txs')}  "
        f"MPP Settled events={snapshot['tempo_mpp']['settled']} "
        f"MPP Settled USD=null  unique_buyers=null  repeat=null",
        file=sys.stderr,
    )
    print("GREEN forbidden. Dune queries this run=0. Codex calls=0.", file=sys.stderr)
    for a in snapshot["alerts"]:
        print(f"[{a['level'].upper()}] {a['id']}: {a['reason']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
