from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from mkr_sky.constants import (
    BINANCE_FALLBACK_URL,
    BINANCE_KLINES_URL,
    MKR_SYMBOL,
    SKY_SYMBOL,
    SUPPORTED_INTERVALS,
)
from mkr_sky.models import Candle, candle_from_binance, candle_from_mapping

GetJson = Callable[[str], Any]

DEFAULT_CACHE_DIR = Path(".cache/klines")
USER_AGENT = "mkr-sky-kline-merge/1.0"


class KlineFetchError(RuntimeError):
    pass


def _http_get_json(url: str, timeout: float = 30.0) -> Any:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            payload = resp.read().decode("utf-8")
    except HTTPError as exc:
        raise KlineFetchError(f"HTTP {exc.code} for {url}") from exc
    except URLError as exc:
        raise KlineFetchError(f"network error for {url}: {exc.reason}") from exc
    return json.loads(payload)


def _klines_url(base: str, symbol: str, interval: str, start_time: int | None, limit: int) -> str:
    params: dict[str, Any] = {"symbol": symbol, "interval": interval, "limit": limit}
    if start_time is not None:
        params["startTime"] = start_time
    return f"{base}?{urlencode(params)}"


def fetch_binance_klines(
    symbol: str,
    interval: str,
    *,
    start_time: int | None = 0,
    get_json: GetJson | None = None,
    sleep_s: float = 0.05,
    limit: int = 1000,
) -> list[Candle]:
    if interval not in SUPPORTED_INTERVALS:
        raise ValueError(f"unsupported interval: {interval}")
    source = "mkr" if symbol.upper().startswith("MKR") else "sky"
    getter = get_json or _http_get_json
    out: list[Candle] = []
    cursor = start_time
    bases = (BINANCE_KLINES_URL, BINANCE_FALLBACK_URL)
    active_base = 0

    while True:
        url = _klines_url(bases[active_base], symbol, interval, cursor, limit)
        try:
            raw = getter(url)
        except KlineFetchError:
            if active_base + 1 < len(bases):
                active_base += 1
                continue
            raise
        if isinstance(raw, dict) and "code" in raw:
            if active_base + 1 < len(bases):
                active_base += 1
                continue
            raise KlineFetchError(str(raw))
        if not raw:
            break
        batch = [candle_from_binance(row, source) for row in raw]
        if cursor:
            batch = [c for c in batch if c.open_time >= cursor]
        if not batch:
            break
        out.extend(batch)
        if len(raw) < limit:
            break
        next_cursor = batch[-1].open_time + 1
        if cursor is not None and next_cursor <= cursor:
            break
        cursor = next_cursor
        if sleep_s:
            time.sleep(sleep_s)
    # Deduplicate in case a retry overlapped.
    uniq: dict[int, Candle] = {}
    for candle in out:
        uniq[candle.open_time] = candle
    return sorted(uniq.values(), key=lambda c: c.open_time)


def _cache_path(cache_dir: Path, symbol: str, interval: str) -> Path:
    return cache_dir / f"{symbol}_{interval}.json"


def _load_cache(path: Path) -> list[Candle]:
    if not path.exists():
        return []
    rows = json.loads(path.read_text(encoding="utf-8"))
    return [candle_from_mapping(row) for row in rows]


def _save_cache(path: Path, candles: list[Candle]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [
        {
            "open_time": c.open_time,
            "open": c.open,
            "high": c.high,
            "low": c.low,
            "close": c.close,
            "volume": c.volume,
            "quote_volume": c.quote_volume,
            "close_time": c.close_time,
            "source": c.source,
        }
        for c in candles
    ]
    path.write_text(json.dumps(payload), encoding="utf-8")


def fetch_symbol_cached(
    symbol: str,
    interval: str,
    *,
    cache_dir: Path | None = DEFAULT_CACHE_DIR,
    get_json: GetJson | None = None,
) -> list[Candle]:
    """Return full history, using on-disk cache for all but the latest bars."""
    if cache_dir is None:
        return fetch_binance_klines(symbol, interval, get_json=get_json)

    path = _cache_path(cache_dir, symbol, interval)
    cached = _load_cache(path)
    start = cached[-2].open_time if len(cached) >= 2 else 0
    fresh = fetch_binance_klines(symbol, interval, start_time=start, get_json=get_json)
    if not fresh:
        return cached
    by_time = {c.open_time: c for c in cached}
    for candle in fresh:
        by_time[candle.open_time] = candle
    merged = sorted(by_time.values(), key=lambda c: c.open_time)
    # Persist everything except the in-progress last bar.
    _save_cache(path, merged[:-1] if merged else merged)
    return merged


def fetch_mkr_and_sky(
    interval: str,
    *,
    cache_dir: Path | None = DEFAULT_CACHE_DIR,
    get_json: GetJson | None = None,
) -> tuple[list[Candle], list[Candle]]:
    mkr = fetch_symbol_cached(MKR_SYMBOL, interval, cache_dir=cache_dir, get_json=get_json)
    sky = fetch_symbol_cached(SKY_SYMBOL, interval, cache_dir=cache_dir, get_json=get_json)
    return mkr, sky
