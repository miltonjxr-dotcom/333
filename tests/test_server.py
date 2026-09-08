from mkr_sky.models import Candle
from mkr_sky.server import app, _series_cache

from fastapi.testclient import TestClient


def _c(t: int, o: float, src: str) -> Candle:
    return Candle(
        open_time=t,
        open=o,
        high=o * 1.01,
        low=o * 0.99,
        close=o,
        volume=10,
        quote_volume=10 * o,
        close_time=t + 1,
        source=src,
    )


def test_klines_api_sky_and_mkr(monkeypatch):
    mkr = (_c(1_000, 2400, "mkr"),)
    sky = (_c(2_000, 0.1, "sky"),)

    def fake_series(interval: str, refresh: bool = False):
        return mkr, sky

    monkeypatch.setattr("mkr_sky.server._series", fake_series)
    _series_cache.clear()
    client = TestClient(app)
    sky_resp = client.get("/api/klines", params={"interval": "1d", "denomination": "sky"})
    assert sky_resp.status_code == 200
    body = sky_resp.json()
    assert body["ratio"] == 24_000
    assert body["merged_bars"] == 2
    assert body["candles"][0]["c"] == 2400 / 24_000
    assert body["candles"][1]["c"] == 0.1

    mkr_resp = client.get("/api/klines", params={"interval": "1d", "denomination": "mkr"})
    assert mkr_resp.json()["candles"][1]["c"] == 0.1 * 24_000

    bad = client.get("/api/klines", params={"interval": "2d"})
    assert bad.status_code == 400
