#!/usr/bin/env python3
"""Public-data tripwire for the agent-economy desk.

Fetches https://agenteconomy.to/data.json and prints a daily brief.

This script is allowed to emit YELLOW flags only.
It must never emit GREEN — green needs a transfer-level sample (playbook §6.3).
Free desk: run scripts/free_quality_panel.py daily; do not spend Dune/Codex here.

August 2026 is the worked false positive: tx count ripped, USD did not.
"""

from __future__ import annotations

import json
import statistics
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from httpjson import get_json

SOURCE = "https://agenteconomy.to/data.json"
Z_WINDOW = 60
TX_Z_YELLOW = 3.0
TICKET_COLLAPSE_WOW = 0.50


def fetch() -> dict[str, Any]:
    return get_json(SOURCE, timeout=30)


def zscore(series: list[float], latest: float) -> float | None:
    hist = series[-Z_WINDOW:-1] if len(series) > 1 else series[:-1]
    if len(hist) < 20:
        return None
    mu = statistics.mean(hist)
    sd = statistics.pstdev(hist)
    if sd == 0:
        return None
    return (latest - mu) / sd


def avg_ticket(month: dict[str, Any]) -> float | None:
    txs = month.get("txs") or 0
    vol = month.get("vol")
    if not txs or vol is None:
        return None
    return vol / txs


def main() -> int:
    data = fetch()
    as_of = data.get("updatedAt") or datetime.now(timezone.utc).isoformat()
    x402 = data["x402"]
    daily = x402.get("daily") or []
    monthly = x402.get("monthly") or []
    mpp = data.get("tempoMpp") or {}
    acp = data.get("virtualsAcp") or {}

    txs_series = [float(d["txs"]) for d in daily if d.get("txs") is not None]
    latest_day = daily[-1] if daily else {}
    # Incomplete UTC day prints as a fake crash (Sep 3 2026: 14k vs prior 1.45M).
    today = date.today().isoformat()
    if (
        len(daily) >= 2
        and latest_day.get("day") == today
        and (latest_day.get("txs") or 0) < 0.2 * (daily[-2].get("txs") or 1)
    ):
        latest_day = daily[-2]
    latest_txs = float(latest_day.get("txs") or 0)
    complete_series = [
        float(d["txs"])
        for d in daily
        if d.get("txs") is not None and d.get("day") != today
    ]
    tx_z = zscore(complete_series, latest_txs) if complete_series else None

    last_month = monthly[-1] if monthly else {}
    prev_month = monthly[-2] if len(monthly) >= 2 else {}
    # Wash-trap compares completed months only (Sep 3 would otherwise look like a crash).
    wash_now, wash_prev = last_month, prev_month
    if date.today().day < 8 and len(monthly) >= 3:
        wash_now, wash_prev = monthly[-2], monthly[-3]
    ticket = avg_ticket(last_month)
    prev_ticket = avg_ticket(prev_month)
    wash_ticket = avg_ticket(wash_now)
    wash_prev_ticket = avg_ticket(wash_prev)

    flags: list[dict[str, str]] = []

    if tx_z is not None and tx_z >= TX_Z_YELLOW:
        flags.append(
            {
                "id": "public_x402_tx_spike",
                "level": "yellow",
                "reason": f"x402 daily txs z={tx_z:.2f} (latest={latest_txs:,.0f}). Unconfirmed. Free panel next; Dune sample only if still yellow after SKU check.",
            }
        )

    if wash_ticket is not None and wash_prev_ticket and wash_prev_ticket > 0:
        drop = 1.0 - (wash_ticket / wash_prev_ticket)
        txs_now = wash_now.get("txs") or 0
        txs_prev = wash_prev.get("txs") or 1
        txs_ratio = txs_now / txs_prev
        if (drop >= TICKET_COLLAPSE_WOW and txs_ratio > 1.0) or (
            txs_ratio >= 2.0 and wash_ticket < wash_prev_ticket
        ):
            flags.append(
                {
                    "id": "S5_wash_trap_public",
                    "level": "yellow",
                    "reason": (
                        f"{wash_now.get('month')} avg ticket ${wash_ticket:.4f} vs "
                        f"{wash_prev.get('month')} ${wash_prev_ticket:.4f} "
                        f"({drop:.0%} change), txs {txs_ratio:.1f}×. Classic wash/campaign "
                        f"pattern (see Aug 2026). Do not treat as adoption."
                    ),
                }
            )

    settled = (mpp.get("byType") or {}).get("Settled")
    events = mpp.get("totalEvents")
    if settled is not None and events:
        ratio = settled / events
        if ratio < 0.05:
            flags.append(
                {
                    "id": "mpp_events_not_settlements",
                    "level": "yellow",
                    "reason": (
                        f"Tempo MPP Settled={settled} / events={events} ({ratio:.2%}). "
                        f"Monitor Settled and unique payees only."
                    ),
                }
            )

    acp_daily = acp.get("daily") or []
    if len(acp_daily) >= 8:
        last7 = acp_daily[-7:]
        prev7 = acp_daily[-14:-7]
        memos_last = sum(d.get("memos") or 0 for d in last7)
        memos_prev = sum(d.get("memos") or 0 for d in prev7) or 1
        senders_last = sum(d.get("senders") or 0 for d in last7)
        senders_prev = sum(d.get("senders") or 0 for d in prev7) or 1
        if memos_last / memos_prev >= 2.0 and senders_last / senders_prev < 1.1:
            flags.append(
                {
                    "id": "M2_memo_theater",
                    "level": "yellow",
                    "reason": "ACP memos doubled WoW without sender breadth. Ignore as commerce.",
                }
            )

    snapshot = {
        "date": date.today().isoformat(),
        "as_of": as_of,
        "quality_available": False,
        "public_tripwire": {
            "x402_daily_txs": latest_txs,
            "x402_daily_txs_z": tx_z,
            "x402_month_avg_ticket": ticket,
            "x402_month": last_month.get("month"),
            "x402_month_txs": last_month.get("txs"),
            "x402_month_vol": last_month.get("vol"),
            "source": SOURCE,
            "note": "T0-like public aggregates only. GREEN is forbidden from this script.",
        },
        "tempo_mpp": {
            "settled": settled,
            "channel_opened": (mpp.get("byType") or {}).get("ChannelOpened"),
            "unique_payers": mpp.get("uniquePayers"),
            "unique_payees": mpp.get("uniquePayees"),
        },
        "virtuals_acp": {
            "memos": acp.get("totalMemos"),
            "latest_day_memos": (acp_daily[-1] or {}).get("memos") if acp_daily else None,
            "latest_day_senders": (acp_daily[-1] or {}).get("senders") if acp_daily else None,
        },
        "alerts": flags,
    }

    json.dump(snapshot, sys.stdout, indent=2)
    sys.stdout.write("\n")

    print("=== DESK BRIEF (unconfirmed) ===", file=sys.stderr)
    print(f"as_of={as_of}  x402_day={latest_day.get('day')} txs={latest_txs:,.0f} z={tx_z}", file=sys.stderr)
    if ticket is not None:
        print(
            f"x402 {last_month.get('month')}: txs={last_month.get('txs')} vol=${last_month.get('vol')} avg_ticket=${ticket:.4f}",
            file=sys.stderr,
        )
    print(f"MPP Settled={settled} payees={mpp.get('uniquePayees')}", file=sys.stderr)
    if not flags:
        print("No yellow flags. Do not produce commentary.", file=sys.stderr)
    for f in flags:
        print(f"[{f['level'].upper()}] {f['id']}: {f['reason']}", file=sys.stderr)
    print("GREEN forbidden on the free desk without a capped Dune sample.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
