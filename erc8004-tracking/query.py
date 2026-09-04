#!/usr/bin/env python3
"""Probe ERC-8004 Identity/Reputation on Base, Ethereum, BNB.

totalSupply() reverts. Count via binary-search ownerOf (monotonic agentId)
plus a small recent eth_getLogs window. Do not sum chains as unique agents.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAP = ROOT / "snapshots"
IDENTITY = "0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
REPUTATION = "0x8004BAa17C55a88189AE136b182e5fdA19dE9b63"
VALIDATION = "0x8004Cc8439f36fd5F9F049D9fF86523Df6dAAB58"
TRANSFER = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
NEW_FEEDBACK = "0x6a4a61743519c9d648a14e6493f47dbe3ff1aa29e7785c96c8326a205e58febc"
VAL_REQ = "0x530436c3634a98e1e626b0898be2f1e9980cc1bd2a78c07a0aba52d0a48a5059"
VAL_RESP = "0xafddf629e874ccc3963b6a888c477bd464a6c8525024fc88759ea3b2326349ae"
ZERO_TOPIC = "0x" + "00" * 32

CHAINS = {
    "base": {"rpc": "https://mainnet.base.org", "chain_id": 8453, "start_hi": 70_000},
    "ethereum": {"rpc": "https://ethereum.publicnode.com", "chain_id": 1, "start_hi": 50_000},
    "bsc": {"rpc": "https://bsc-dataseed.binance.org", "chain_id": 56, "start_hi": 300_000},
}


def rpc(url: str, method: str, params, timeout: int = 30, retries: int = 4):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json", "User-Agent": "erc8004-tracking/1.0"}
    )
    last = None
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            last = e
            time.sleep(0.4 * (i + 1))
    raise RuntimeError(f"{url} {method} failed: {last}")


def owner_of(url: str, token_id: int):
    data = "0x6352211e" + hex(token_id)[2:].rjust(64, "0")
    out = rpc(url, "eth_call", [{"to": IDENTITY, "data": data}, "latest"])
    if out.get("error") or not out.get("result") or out["result"] == "0x":
        return None
    owner = "0x" + out["result"][-40:]
    if owner == "0x" + "00" * 20:
        return None
    return owner


def binary_max(url: str, start_hi: int) -> int:
    if owner_of(url, 1) is None:
        return 0
    hi = max(start_hi, 1)
    while owner_of(url, hi) is not None:
        hi *= 2
        if hi > 5_000_000:
            break
        time.sleep(0.04)
    left, right, last = 1, hi, 1
    while left <= right:
        mid = (left + right) // 2
        if owner_of(url, mid) is not None:
            last = mid
            left = mid + 1
        else:
            right = mid - 1
        time.sleep(0.03)
    return last


def nlogs(url: str, address: str, topics: list, from_block: int) -> int | str:
    try:
        out = rpc(
            url,
            "eth_getLogs",
            [{"address": address, "fromBlock": hex(from_block), "toBlock": "latest", "topics": topics}],
        )
    except Exception as e:
        return f"error: {e}"
    if out.get("error"):
        return f"error: {out['error']}"
    return len(out.get("result") or [])


def probe_chain(name: str, cfg: dict) -> dict:
    url = cfg["rpc"]
    try:
        block = int(rpc(url, "eth_blockNumber", [])["result"], 16)
    except Exception as e:
        return {"chain": name, "error": str(e)}
    window = 2_000
    mx = binary_max(url, cfg["start_hi"])
    from_block = max(block - window, 0)
    return {
        "chain": name,
        "chain_id": cfg["chain_id"],
        "block": block,
        "max_agent_id_ownerOf": mx,
        "owner_of_1": owner_of(url, 1),
        "owner_of_max": owner_of(url, mx) if mx else None,
        "owner_of_max_plus_1": owner_of(url, mx + 1) if mx else None,
        "recent_window_blocks": window,
        "recent_mints_transfer_from_zero": nlogs(url, IDENTITY, [TRANSFER, ZERO_TOPIC], from_block),
        "recent_new_feedback": nlogs(url, REPUTATION, [NEW_FEEDBACK], from_block),
        "recent_validation_request": nlogs(url, VALIDATION, [VAL_REQ], from_block),
        "recent_validation_response": nlogs(url, VALIDATION, [VAL_RESP], from_block),
        "caveat": "max_agent_id assumes sequential mint; confirm with a mint log tokenId near max.",
    }


def main() -> None:
    SNAP.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    chains = [probe_chain(n, c) for n, c in CHAINS.items()]
    out = {
        "captured_at": now.isoformat(),
        "identity": IDENTITY,
        "reputation": REPUTATION,
        "validation_scanned": VALIDATION,
        "validation_note": "Official explorer: mainnet Validation pending. This address is scanned for events only.",
        "do_not_sum_chains": True,
        "totalSupply_reverts": True,
        "chains": chains,
        "dashboard_check_agenteconomy_2026_08_26": {
            "total_agents_24_chains": 509272,
            "bnb": 299326,
            "base": 70113,
            "ethereum": 68231,
            "note": "Compare per-chain to ownerOf max. Ethereum dashboard was already too high vs ownerOf(68231) revert.",
        },
    }
    path = SNAP / f"{now.date().isoformat()}.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(path)
    for c in chains:
        print(c.get("chain"), "max", c.get("max_agent_id_ownerOf"), "err", c.get("error"))


if __name__ == "__main__":
    main()
