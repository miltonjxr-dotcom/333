#!/usr/bin/env python3
"""Daily BlockRun / PayAI snapshot. JSON-only sources; x402scan HTML is filled by hand/WebFetch."""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAP = ROOT / "snapshots"
PAYAI_STATS = "https://facilitator.payai.network/discovery/stats"
SOLANA_RPC = "https://api.mainnet-beta.solana.com"
# Previously seen as the 24h firehose on sol.blockrun.ai (verify merchant vs payer daily).
WATCH = [
    "BhFRCUXHVm76PmXkSzus8T4LUGrD2MTW9Au6bocBox5U",
]


def get_json(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": "blockrun-tracking/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def rpc(method: str, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(
        SOLANA_RPC, data=body, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def wallet_pulse(addr: str) -> dict:
    sigs = (rpc("getSignaturesForAddress", [addr, {"limit": 20}]).get("result") or [])
    bal = (rpc("getBalance", [addr]).get("result") or {}).get("value")
    ta = rpc(
        "getTokenAccountsByOwner",
        [
            addr,
            {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
            {"encoding": "jsonParsed"},
        ],
    )
    usdc = "0"
    for a in (ta.get("result") or {}).get("value") or []:
        info = a["account"]["data"]["parsed"]["info"]
        if info.get("mint") == "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v":
            usdc = info.get("tokenAmount", {}).get("uiAmountString", "0")
    times = [s.get("blockTime") for s in sigs if s.get("blockTime")]
    gaps = []
    for i in range(len(times) - 1):
        if times[i] and times[i + 1]:
            gaps.append(times[i] - times[i + 1])
    return {
        "address": addr,
        "sol_lamports": bal,
        "usdc": usdc,
        "recent_sigs": len(sigs),
        "recent_errors": sum(1 for s in sigs if s.get("err")),
        "newest_block_time": times[0] if times else None,
        "median_gap_sec_recent20": sorted(gaps)[len(gaps) // 2] if gaps else None,
        "note": "confirm merchant vs payer before treating as a user",
    }


def main() -> None:
    SNAP.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    payai = get_json(PAYAI_STATS)
    top = payai.get("topMerchants") or []
    blockrun_rows = [m for m in top if "blockrun" in str(m.get("resourceHost", "")).lower()]
    out = {
        "captured_at": now.isoformat(),
        "payai_stats": {
            "cached_at": payai.get("cachedAt"),
            "settlements_24h": (payai.get("settlements") or {}).get("last24h"),
            "settlements_7d": (payai.get("settlements") or {}).get("last7d"),
            "settlements_30d": (payai.get("settlements") or {}).get("last30d"),
            "hosts": (payai.get("merchants") or {}).get("hosts"),
            "blockrun_in_top_merchants": blockrun_rows,
            "caveat": "PayAI buckets (50K+) disagree with x402scan daily millions; do not use buckets for share.",
        },
        "x402scan": {
            "sol_blockrun": {
                "tx_24h": None,
                "volume_usd_24h": None,
                "buyers_24h": None,
                "tx_30d": None,
                "volume_usd_30d": None,
                "buyers_30d": None,
                "source": "fill from https://www.x402scan.com/ (sol.blockrun.ai)",
            },
            "base_blockrun": {
                "tx_24h": None,
                "volume_usd_24h": None,
                "buyers_24h": None,
                "tx_30d": None,
                "volume_usd_30d": None,
                "buyers_30d": None,
                "source": "fill from blockrun.ai server page",
            },
            "payai_facilitator_24h": {
                "tx": None,
                "volume_usd": None,
                "buyers": None,
                "sellers": None,
                "source": "https://www.x402scan.com/facilitator/payAI",
            },
        },
        "watch_wallets": [wallet_pulse(a) for a in WATCH],
        "labels_today": [],
        "notes": "",
    }
    path = SNAP / f"{now.date().isoformat()}.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(path)


if __name__ == "__main__":
    main()
