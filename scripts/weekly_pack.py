#!/usr/bin/env python3
"""Auto-fill the weekly 表 0 from free JSON. No Dune, no Codex, no Artemis scrape.

Prints a markdown pack to stdout. Human leftover is ~10 minutes of eyeball pages
that have no public dump (Artemis, OpenRouter rankings).

  python3 scripts/weekly_pack.py
  python3 scripts/weekly_pack.py --json
  python3 scripts/weekly_pack.py --save data/weekly
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from free_quality_panel import (  # noqa: E402
    AGENT_JSON,
    build_panel,
    catalog_seller_counts,
    load_x402watch_json,
    load_x402watch_services,
    sku_from_category_benchmarks,
)
from httpjson import get_json  # noqa: E402
from tripwire import avg_ticket, zscore  # noqa: E402

NPM_WEEK = "https://api.npmjs.org/downloads/point/last-week/x402"
NPM_PREV = "https://api.npmjs.org/downloads/point/last-month/x402"
X402_LIST = "https://x402-list.com/api/v1/facilitators"
ARTEMIS = "https://www.artemis.ai/sectors/agentic-payments"
OPENROUTER = "https://openrouter.ai/rankings"
X402SCAN = "https://www.x402scan.com"

PROXY_MOVE_PCT = 0.30
T0_CAMPAIGN_TX_WOW = 1.0  # 2× last 7d vs prior 7d
TICKET_CAMPAIGN = 0.05


def _pct(now: float | None, then: float | None) -> float | None:
    if now is None or then is None or then == 0:
        return None
    return (now - then) / abs(then)


def _moved(pct: float | None, threshold: float = PROXY_MOVE_PCT) -> bool:
    return pct is not None and abs(pct) >= threshold


def _fmt_usd(x: float | None) -> str:
    if x is None:
        return "null"
    return f"${x:,.2f}"


def _fmt_n(x: Any) -> str:
    if x is None:
        return "null"
    if isinstance(x, float):
        return f"{x:,.0f}"
    return f"{x:,}"


def _fmt_pct(p: float | None) -> str:
    if p is None:
        return "n/a"
    sign = "+" if p >= 0 else ""
    return f"{sign}{p:.0%}"


def complete_x402_days(daily: list[dict[str, Any]]) -> list[dict[str, Any]]:
    today = date.today().isoformat()
    out: list[dict[str, Any]] = []
    for i, d in enumerate(daily):
        txs = d.get("txs") or 0
        if d.get("day") == today and i == len(daily) - 1:
            prev = daily[i - 1].get("txs") or 1 if i else 1
            if txs < 0.2 * prev:
                continue
        out.append(d)
    return out


def window_txs(daily: list[dict[str, Any]], start: int, end: int | None) -> int:
    chunk = daily[start:end]
    return int(sum(d.get("txs") or 0 for d in chunk))


def wow_sku_and_sellers(snap_day: date) -> dict[str, Any]:
    prev_day = snap_day - timedelta(days=7)
    cats = load_x402watch_json("category-benchmarks", prev_day)
    services = load_x402watch_services(prev_day)
    out: dict[str, Any] = {"compare_date": prev_day.isoformat()}
    if cats:
        rows, usd, txs, _rollup = sku_from_category_benchmarks(cats)
        out["f_sku_usd_24h"] = usd
        out["f_sku_txs_24h"] = txs
        out["top_category"] = rows[0]["category"] if rows else None
        out["top_share"] = (rows[0]["usd"] / usd) if rows and usd else None
    live, named, _acp = catalog_seller_counts(services, prev_day)
    out["live_named_sellers_7d"] = named
    out["live_sellers_7d"] = live
    return out


def npm_x402() -> dict[str, Any] | None:
    try:
        week = get_json(NPM_WEEK)
        month = get_json(NPM_PREV)
    except Exception:
        return None
    return {
        "last_week_downloads": week.get("downloads"),
        "last_week_range": [week.get("start"), week.get("end")],
        "last_month_downloads": month.get("downloads"),
        "note": "Developer funnel only. Not Service Spend.",
    }


def facilitator_floor() -> dict[str, Any] | None:
    try:
        blob = get_json(X402_LIST)
    except Exception:
        return None
    rows = blob.get("data") or []
    cleaned = []
    for r in rows:
        cleaned.append(
            {
                "name": r.get("name") or r.get("facilitator_id"),
                "volume_usd_7d": r.get("volume_usd_7d"),
                "tx_count_7d": r.get("tx_count_7d"),
            }
        )
    cleaned.sort(key=lambda r: float(r.get("volume_usd_7d") or 0), reverse=True)
    return {
        "top3_7d": cleaned[:3],
        "note": (
            "USDC settler-address floor (CC BY 4.0). Not ecosystem GMV. "
            "Do not add into 表 0. Virtuals settler flow is ACP-shaped."
        ),
    }


def classify(
    *,
    sku_wow: float | None,
    settled_wow: float | None,
    sellers_wow: float | None,
    t0_wow: float | None,
    ticket: float | None,
    sku_top_share: float | None,
    sku_usd: float,
    settled_now: int | None,
    settled_then: int | None,
) -> dict[str, Any]:
    sku_moved = _moved(sku_wow)
    settled_moved = _moved(settled_wow)
    sellers_moved = _moved(sellers_wow)
    proxy_moved = sku_moved or settled_moved or sellers_moved
    t0_ripped = t0_wow is not None and t0_wow >= T0_CAMPAIGN_TX_WOW
    campaign = bool(
        (t0_ripped and not proxy_moved)
        or (ticket is not None and ticket < TICKET_CAMPAIGN and t0_ripped)
        or (sku_usd > 0 and sku_top_share is not None and sku_top_share >= 0.50 and not settled_moved)
    )
    if not proxy_moved and not t0_ripped:
        mode = "quiet"
        open_12 = False
        line2 = "代理与 T0 都没明显动 → 只扫表 6"
    elif campaign and not proxy_moved:
        mode = "campaign"
        open_12 = False
        line2 = "仅 T0 笔数动、F_sku / Settled / sellers 不动 → 战役，不要研究仓位"
    elif campaign and sku_top_share and sku_top_share >= 0.50:
        mode = "sku_cluster"
        open_12 = True
        line2 = "F_sku 单类目 ≥50% → covered-SKU 集群，不是 S1；表 1/2 可看一眼代理"
    elif proxy_moved:
        mode = "proxy_moved"
        open_12 = True
        line2 = "F_sku 或 Settled 或 catalog sellers 动了 → 打开表 1/2 看代理，仍不是 GMV"
    else:
        mode = "watch"
        open_12 = False
        line2 = "未分类清楚；默认当战役/安静，不升级"

    # Cumulative Settled that never changes still "not moved".
    if settled_now is not None and settled_then is not None and settled_now == settled_then:
        settled_moved = False

    return {
        "mode": mode,
        "open_table_1_2": open_12,
        "burn_dune": False,
        "investable": False,
        "line2": line2,
        "proxy_moved": proxy_moved,
        "campaign": campaign,
        "sku_moved": sku_moved,
        "settled_moved": settled_moved,
        "sellers_moved": sellers_moved,
    }


def render_md(pack: dict[str, Any]) -> str:
    t0 = pack["table0"]
    c = pack["conclusion"]
    wow = pack["wow"]
    npm = pack.get("npm_x402") or {}
    fac = pack.get("facilitator_floor") or {}
    alerts = pack.get("alerts") or []
    lines = [
        f"# Agent economy 表 0 — {pack['week_of']}",
        "",
        f"生成时间 `{pack['as_of']}` · `quality_available: false` · "
        f"Dune={pack['quota']['dune_queries_this_run']} · Codex={pack['quota']['codex_calls_this_run']}",
        "",
        "Observed Service Spend 必须是 **null**。下面的美元和笔数**不要加总**。",
        "",
        "| 格 | 本周 | 一周前 | 变动 | 量纲 |",
        "| --- | --- | --- | --- | --- |",
        f"| Observed Service Spend | **null** | **null** | — | USD |",
        f"| x402 covered SKU proxy | {_fmt_usd(t0['f_sku_usd_24h'])} | {_fmt_usd(wow['f_sku_usd_24h'])} | {_fmt_pct(wow['f_sku_usd_wow'])} | USD |",
        f"| 其中最大类目 | {t0.get('top_category') or 'n/a'} {_fmt_pct(t0.get('top_share')).replace('+','') if t0.get('top_share') is not None else ''} | {wow.get('top_category') or 'n/a'} | — | — |",
        f"| MPP settled paid events | {_fmt_n(t0['mpp_settled_paid_events'])} | {_fmt_n(wow['mpp_settled_paid_events'])} | {_fmt_pct(wow['mpp_settled_wow'])} | count |",
        f"| MPP settled USD | **null** | **null** | — | USD |",
        f"| Unique Buyers | **null** | **null** | — | — |",
        f"| Repeat | **null** | **null** | — | — |",
        f"| Catalog named sellers 7d | {_fmt_n(t0['live_named_sellers_7d'])} | {_fmt_n(wow['live_named_sellers_7d'])} | {_fmt_pct(wow['sellers_wow'])} | count |",
        f"| T0 last-7d txs（战役探测器） | {_fmt_n(t0['t0_txs_7d'])} | {_fmt_n(wow['t0_txs_7d'])} | {_fmt_pct(wow['t0_txs_wow'])} | count |",
        f"| T0 month avg ticket | {_fmt_usd(t0['t0_month_avg_ticket'])} | {_fmt_usd(wow['t0_prev_month_avg_ticket'])} | — | USD/tx |",
        "",
        "## 自动结论（脚本写的，不是绿灯）",
        "",
        "1. Observed Spend：**null**",
        f"2. 战役还是代理在动：{c['line2']}",
        f"3. 要不要打开表 1/2：**{'是' if c['open_table_1_2'] else '否'}**",
        "4. 要不要烧 Dune：**否**（默认；黄灯仍看不懂再 ≤3 条抽样）",
        "5. 有没有可投资表达：**无**（质量门未过，禁止从 T0/F_sku 映射仓位）",
        "",
        f"mode=`{c['mode']}`",
        "",
        "## 仍需人工（约 10 分钟，无公开 JSON）",
        "",
        f"- [ ] Artemis Real vs Gamed 方向（不当 T3）：{ARTEMIS}",
        f"- [ ] OpenRouter rankings 推理是否同向：{OPENROUTER}",
        f"- [ ] x402scan 30d 原始目录对照：{X402SCAN}",
        "- [ ] 表 6 日历：Arc / AP2 / 拒付归因 / 公约，无则写无",
        "",
        "## 旁证（不是表 0）",
        "",
        f"- npm `x402` last-week downloads: {_fmt_n(npm.get('last_week_downloads'))} "
        f"({(npm.get('last_week_range') or ['?', '?'])[0]} → {(npm.get('last_week_range') or ['?', '?'])[1]})",
    ]
    top3 = fac.get("top3_7d") or []
    if top3:
        bits = ", ".join(
            f"{r['name']} 7d {_fmt_usd(r.get('volume_usd_7d'))}" for r in top3
        )
        lines.append(f"- x402-list settler **floor** top3（勿加进表 0）：{bits}")
        lines.append(f"- {fac.get('note')}")
    lines += [
        "",
        "## 黄灯",
        "",
    ]
    if not alerts:
        lines.append("无。不要写评述。")
    else:
        for a in alerts:
            lines.append(f"- **{a.get('level', '').upper()}** `{a.get('id')}`: {a.get('reason')}")
    lines += [
        "",
        "禁止：自建 Dune 仪表盘当周更、把首页美元加总成 Agent Economy GDP、把 F_sku 美元与 Settled 笔数相加。",
        "",
    ]
    return "\n".join(lines)


def build_pack() -> dict[str, Any]:
    panel = build_panel()
    agent = get_json(AGENT_JSON)
    snap_day = date.fromisoformat(panel["free_proxy"]["x402watch_snapshot_date"])
    prev = wow_sku_and_sellers(snap_day)

    daily = complete_x402_days((agent.get("x402") or {}).get("daily") or [])
    t0_now_7 = window_txs(daily, -7, None) if len(daily) >= 7 else window_txs(daily, 0, None)
    t0_prev_7 = window_txs(daily, -14, -7) if len(daily) >= 14 else None

    monthly = (agent.get("x402") or {}).get("monthly") or []
    last_m = monthly[-1] if monthly else {}
    prev_m = monthly[-2] if len(monthly) >= 2 else {}
    if date.today().day < 8 and len(monthly) >= 3:
        last_m, prev_m = monthly[-2], monthly[-3]

    sku_now = float(panel["free_proxy"]["f_sku_usd_24h"] or 0)
    sku_then = prev.get("f_sku_usd_24h")
    sku_wow = _pct(sku_now, sku_then)

    settled_now = panel["tempo_mpp"].get("settled_paid_events")
    # Cumulative headline has no 7d series. Compare only if we have a prior pack later;
    # for a first run, WoW on the 384-style total is unknown.
    settled_then = None
    settled_wow = None

    sellers_now = panel["free_proxy"].get("live_named_sellers_7d")
    sellers_then = prev.get("live_named_sellers_7d")
    sellers_wow = _pct(
        float(sellers_now) if sellers_now is not None else None,
        float(sellers_then) if sellers_then is not None else None,
    )
    t0_wow = _pct(float(t0_now_7), float(t0_prev_7) if t0_prev_7 else None)

    sku_rows = panel["free_proxy"].get("f_sku_24h_by_category") or []
    top = sku_rows[0] if sku_rows else {}
    top_share = (float(top.get("usd") or 0) / sku_now) if sku_now else None

    ticket = avg_ticket(last_m)
    txs_series = [float(d["txs"]) for d in daily if d.get("txs") is not None]
    latest_txs = float(panel["public_tripwire"].get("x402_daily_txs") or 0)
    tx_z = zscore(txs_series, latest_txs) if txs_series else None

    conclusion = classify(
        sku_wow=sku_wow,
        settled_wow=settled_wow,
        sellers_wow=sellers_wow,
        t0_wow=t0_wow,
        ticket=ticket,
        sku_top_share=top_share,
        sku_usd=sku_now,
        settled_now=settled_now,
        settled_then=settled_then,
    )

    pack = {
        "week_of": date.today().isoformat(),
        "as_of": panel.get("as_of") or datetime.now(timezone.utc).isoformat(),
        "quality_available": False,
        "observed_service_spend_usd": None,
        "quota": {"dune_queries_this_run": 0, "codex_calls_this_run": 0},
        "table0": {
            "observed_service_spend_usd": None,
            "f_sku_usd_24h": sku_now,
            "top_category": top.get("category"),
            "top_share": top_share,
            "mpp_settled_paid_events": settled_now,
            "mpp_settled_usd": None,
            "unique_buyers": None,
            "repeat_buyer_rate": None,
            "live_named_sellers_7d": sellers_now,
            "t0_txs_7d": t0_now_7,
            "t0_month_avg_ticket": ticket,
            "t0_month": last_m.get("month"),
        },
        "wow": {
            "compare_sku_date": prev.get("compare_date"),
            "f_sku_usd_24h": sku_then,
            "f_sku_usd_wow": sku_wow,
            "top_category": prev.get("top_category"),
            "mpp_settled_paid_events": settled_then,
            "mpp_settled_wow": settled_wow,
            "mpp_settled_wow_note": "Settled is a cumulative headline with no daily Settled series; WoW stays null.",
            "live_named_sellers_7d": sellers_then,
            "sellers_wow": sellers_wow,
            "t0_txs_7d": t0_prev_7,
            "t0_txs_wow": t0_wow,
            "t0_prev_month_avg_ticket": avg_ticket(prev_m),
            "t0_daily_txs_z": tx_z,
        },
        "conclusion": conclusion,
        "alerts": list(panel.get("alerts") or []),
        "npm_x402": npm_x402(),
        "facilitator_floor": facilitator_floor(),
        "eyeball_required": [
            {"id": "artemis", "url": ARTEMIS, "job": "Real vs Gamed direction; not T3"},
            {"id": "openrouter", "url": OPENROUTER, "job": "inference corroboration"},
            {"id": "x402scan", "url": X402SCAN, "job": "raw 30d catalog vs T0"},
        ],
        "panel": panel,
    }
    if tx_z is not None and tx_z >= 3.0:
        pack["alerts"].append(
            {
                "id": "public_x402_tx_spike",
                "level": "yellow",
                "reason": f"x402 daily txs z={tx_z:.2f}. Unconfirmed campaign detector.",
            }
        )
    return pack


def main() -> int:
    ap = argparse.ArgumentParser(description="Auto-fill weekly 表 0 (free desk).")
    ap.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    ap.add_argument("--save", metavar="DIR", help="Write week-of.md and week-of.json")
    args = ap.parse_args()
    pack = build_pack()
    md = render_md(pack)
    if args.json:
        json.dump(pack, sys.stdout, indent=2, default=str)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(md)
        if not md.endswith("\n"):
            sys.stdout.write("\n")
    if args.save:
        dest = Path(args.save)
        dest.mkdir(parents=True, exist_ok=True)
        stem = pack["week_of"]
        (dest / f"{stem}.md").write_text(md, encoding="utf-8")
        (dest / f"{stem}.json").write_text(
            json.dumps(pack, indent=2, default=str) + "\n", encoding="utf-8"
        )
        print(f"saved {dest / stem}.md", file=sys.stderr)
    print(
        f"mode={pack['conclusion']['mode']}  open_1_2={pack['conclusion']['open_table_1_2']}  "
        f"Dune=0 Codex=0  Observed Spend=null",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
