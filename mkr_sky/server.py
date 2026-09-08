from __future__ import annotations

import time
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from mkr_sky.constants import CUTOVER_MS, DENOMINATIONS, RATIO, SUPPORTED_INTERVALS
from mkr_sky.fetch import KlineFetchError, fetch_mkr_and_sky
from mkr_sky.merge import merge_klines, splice_quality
from mkr_sky.models import Candle

WEB_DIR = Path(__file__).resolve().parent.parent / "web"
CACHE_TTL_S = 60.0

app = FastAPI(title="MKR × SKY merged klines", version="1.0.0")

_series_cache: dict[str, tuple[float, tuple[Candle, ...], tuple[Candle, ...]]] = {}


def _series(interval: str, refresh: bool = False) -> tuple[tuple[Candle, ...], tuple[Candle, ...]]:
    now = time.time()
    hit = _series_cache.get(interval)
    if hit and not refresh and now - hit[0] < CACHE_TTL_S:
        return hit[1], hit[2]
    mkr, sky = fetch_mkr_and_sky(interval)
    packed = (now, tuple(mkr), tuple(sky))
    _series_cache[interval] = packed
    return packed[1], packed[2]


def _load(interval: str, denomination: str, refresh: bool = False):
    if interval not in SUPPORTED_INTERVALS:
        raise HTTPException(400, f"unsupported interval: {interval}")
    if denomination not in DENOMINATIONS:
        raise HTTPException(400, f"unsupported denomination: {denomination}")
    try:
        mkr, sky = _series(interval, refresh=refresh)
    except KlineFetchError as exc:
        raise HTTPException(502, str(exc)) from exc
    candles = merge_klines(mkr, sky, denomination=denomination)
    quality = splice_quality(mkr, sky)
    cutover = sky[0].open_time if sky else CUTOVER_MS
    return {
        "ratio": RATIO,
        "interval": interval,
        "denomination": denomination,
        "cutover_ms": cutover,
        "mkr_bars": len(mkr),
        "sky_bars": len(sky),
        "merged_bars": len(candles),
        "splice": quality,
        "candles": [c.to_api() for c in candles],
    }


@app.get("/api/klines")
def api_klines(
    interval: str = Query("1d"),
    denomination: str = Query("sky"),
    refresh: bool = Query(False),
):
    return _load(interval, denomination, refresh=refresh)


@app.get("/api/meta")
def api_meta(interval: str = Query("1d")):
    payload = _load(interval, "sky")
    payload.pop("candles", None)
    return payload


@app.get("/")
def index():
    index_path = WEB_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(500, "web UI is missing")
    return FileResponse(index_path)


if WEB_DIR.exists():
    app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")
