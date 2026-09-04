#!/usr/bin/env python3
"""Weekly x402 + Tempo MPP snapshot. JSON-only sources; x402scan HTML is filled by hand."""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAP = ROOT / "snapshots"
UA = "x402-mpp-tracking/1.0"
PAYAI_STATS = "https://facilitator.payai.network/discovery/stats"
X402WATCH = "https://api.x402.printmoneylab.com/api/v1"
AE_DATA = "https://agenteconomy.to/data.json"


def get_json(url: str, timeout: int = 40):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def safe(url: str):
    try:
        return get_json(url)
    except Exception as e:
        return {"_error": f"{type(e).__name__}: {e}"}


def slim_categories(payload: dict) -> dict:
    cats = []
    for c in (payload.get("categories") or [])[:20]:
        cats.append(
            {
                "category": c.get("category"),
                "services_count": c.get("services_count"),
                "volume_24h": c.get("volume_24h"),
                "tx_24h": c.get("tx_24h"),
                "real_volume_pct": c.get("real_volume_pct"),
                "wash_pct": c.get("wash_pct"),
                "label_distribution": c.get("label_distribution"),
            }
        )
    return {
        "total_categories": payload.get("total_categories"),
        "total_services": payload.get("total_services"),
        "total_volume_24h": payload.get("total_volume_24h"),
        "total_tx_24h": payload.get("total_tx_24h"),
        "last_updated": payload.get("last_updated"),
        "top": cats,
        "caveat": "This catalog omits Solana BlockRun-scale firehoses. Do not add to x402scan USD.",
    }


def slim_mpp(payload: dict) -> dict:
    m = (payload or {}).get("tempoMpp") or {}
    if not m:
        return {"_error": "tempoMpp missing", "keys": list((payload or {}).keys())[:20]}
    daily = m.get("daily") or []
    last7 = daily[-7:]
    return {
        "total_events": m.get("totalEvents"),
        "unique_payers": m.get("uniquePayers"),
        "unique_payees": m.get("uniquePayees"),
        "by_type": m.get("byType"),
        "settled_share": (
            (m.get("byType") or {}).get("Settled", 0) / m["totalEvents"]
            if m.get("totalEvents")
            else None
        ),
        "last7": last7,
        "last7_events": sum(r.get("events") or 0 for r in last7),
        "last7_max_daily_payers": max((r.get("payers") or 0) for r in last7) if last7 else None,
        "caveat": "Channel events, not USD. Cumulative payers ≠ this week's active payers.",
    }


def main() -> None:
    SNAP.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    payai = safe(PAYAI_STATS)
    landing = safe(f"{X402WATCH}/landing-stats")
    wash = safe(f"{X402WATCH}/wash-report")
    cats = safe(f"{X402WATCH}/categories")
    ae = safe(AE_DATA)

    settlements = (payai.get("settlements") or {}) if isinstance(payai, dict) else {}
    out = {
        "captured_at": now.isoformat(),
        "rails_do_not_sum": [
            "x402 raw settlement (x402scan / PayAI)",
            "x402 wash-filtered catalog (x402watch)",
            "Tempo MPP channel events (agenteconomy tempoMpp)",
        ],
        "payai_stats": {
            "cached_at": payai.get("cachedAt") if isinstance(payai, dict) else None,
            "settlements_24h": settlements.get("last24h"),
            "settlements_7d": settlements.get("last7d"),
            "settlements_30d": settlements.get("last30d"),
            "error": payai.get("_error"),
            "caveat": "Do not use PayAI 50K+ merchant buckets for share.",
        },
        "x402watch": {
            "landing": {
                "stats": (landing.get("stats") if isinstance(landing, dict) else None),
                "label_distribution_all": (
                    landing.get("label_distribution") if isinstance(landing, dict) else None
                ),
                "error": landing.get("_error") if isinstance(landing, dict) else None,
                "note": "landing label_distribution is broader than 30d active; prefer wash-report for weekly buyers.",
            },
            "wash_report": {
                "stats": wash.get("stats") if isinstance(wash, dict) else None,
                "label_distribution_30d": (
                    wash.get("label_distribution") if isinstance(wash, dict) else None
                ),
                "error": wash.get("_error") if isinstance(wash, dict) else None,
            },
            "categories": slim_categories(cats) if isinstance(cats, dict) and "categories" in cats else cats,
        },
        "tempo_mpp": slim_mpp(ae) if isinstance(ae, dict) and "_error" not in ae else ae,
        "x402scan": {
            "payai_facilitator_24h": {
                "tx": None,
                "volume_usd": None,
                "buyers": None,
                "sellers": None,
                "source": "https://www.x402scan.com/facilitator/payAI",
            },
            "coinbase_facilitator_24h": {
                "tx": None,
                "volume_usd": None,
                "buyers": None,
                "sellers": None,
                "source": "https://www.x402scan.com/facilitator/coinbase",
            },
            "sol_blockrun_24h": {
                "tx": None,
                "volume_usd": None,
                "buyers": None,
                "source": "https://www.x402scan.com/ (sol.blockrun.ai); may copy blockrun-tracking snapshot",
            },
        },
        "stripe_offchain_mpp": {
            "disclosed": False,
            "note": "Card / SPT sessions are opaque unless Stripe or Tempo publishes them.",
        },
        "dual_rail": [],
        "notes": "",
    }

    path = SNAP / f"{now.date().isoformat()}.json"
    if path.exists():
        old = json.loads(path.read_text())
        for key in ("x402scan", "dual_rail", "notes", "stripe_offchain_mpp"):
            if old.get(key) and not _has_values(out.get(key)):
                out[key] = old[key]
            elif key in ("dual_rail", "notes") and old.get(key):
                out[key] = old[key]
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(path)


def _has_values(node) -> bool:
    if node is None:
        return False
    if isinstance(node, dict):
        return any(_has_values(v) for k, v in node.items() if k not in ("source", "note", "notes"))
    if isinstance(node, list):
        return any(_has_values(v) for v in node)
    if isinstance(node, bool):
        return node
    return True


if __name__ == "__main__":
    main()
