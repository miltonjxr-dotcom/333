#!/usr/bin/env python3
"""Refresh public x402 protocol snapshots.

Main-market totals come from agenteconomy (Dune-backed facilitator settlements).
Robinhood (eip155:4663) is not in that feed; this script pulls Canopy/Primer/Dexter
/supported plus Blockscout counters for the Exact Permit2 proxy and known relayers.
"""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "raw"
UA = "x402-snapshot/1.0 (+research)"


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def save(name: str, body: bytes) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_bytes(body)
    print("wrote", name, len(body))


def main() -> None:
    save("agenteconomy.json", get("https://agenteconomy.to/data.json"))
    save("canopy-status.json", get("https://facilitator.canopyfinance.io/status"))
    save("canopy-discovery.json", get("https://facilitator.canopyfinance.io/discovery"))
    save("canopy-supported.json", get("https://facilitator.canopyfinance.io/supported"))
    save("payai-supported.json", get("https://facilitator.payai.network/supported"))
    save("primer-supported.json", get("https://x402.primer.systems/supported"))
    save("dexter-supported.json", get("https://x402.dexter.cash/supported"))
    save("dexter-health.json", get("https://x402.dexter.cash/health"))
    print("asOf", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
