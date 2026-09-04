"""Fetch JSON over HTTP. Vercel often serves brotli; stdlib urllib may not decode it."""

from __future__ import annotations

import gzip
import json
import subprocess
import urllib.request
from typing import Any

UA = "agent-economy-monitor/1.0 (free-desk)"


def _looks_json(data: bytes) -> bool:
    i = 0
    while i < len(data) and data[i] in b" \t\r\n":
        i += 1
    return i < len(data) and data[i] in b"{["


def get_bytes(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            enc = (resp.headers.get("Content-Encoding") or "").lower()
            if enc in ("gzip", "x-gzip"):
                data = gzip.decompress(data)
            elif enc == "deflate":
                import zlib

                data = zlib.decompress(data)
    except Exception:
        data = b""
    if _looks_json(data) or data[:2] == b"\x1f\x8b":
        return data
    return subprocess.check_output(
        ["curl", "-fsSL", "--compressed", "-A", UA, url],
        timeout=timeout,
    )


def get_json(url: str, timeout: int = 60) -> dict[str, Any]:
    return json.loads(get_bytes(url, timeout=timeout).decode("utf-8"))
