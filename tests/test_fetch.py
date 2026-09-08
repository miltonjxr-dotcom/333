from urllib.parse import parse_qs, urlparse

from mkr_sky.fetch import fetch_binance_klines
from mkr_sky.merge import merge_klines


def _row(open_time: int, price: str, volume: str) -> list:
    return [
        open_time,
        price,
        price,
        price,
        price,
        volume,
        open_time + 3_599_999,
        "100",
        10,
        "0",
        "0",
        "0",
    ]


def test_fetch_paginates_and_dedupes():
    calls = []

    def get_json(url: str):
        calls.append(url)
        qs = parse_qs(urlparse(url).query)
        symbol = qs["symbol"][0]
        start = int(qs.get("startTime", ["0"])[0])
        if symbol == "MKRUSDT":
            rows = [_row(1_000, "24000", "1"), _row(2_000, "24100", "1"), _row(3_000, "24200", "1")]
        else:
            rows = [_row(4_000, "1.01", "100")]
        page = [row for row in rows if row[0] >= start][:2]
        return page

    mkr = fetch_binance_klines("MKRUSDT", "1h", get_json=get_json, sleep_s=0, limit=2)
    sky = fetch_binance_klines("SKYUSDT", "1h", get_json=get_json, sleep_s=0, limit=2)
    assert [c.open_time for c in mkr] == [1_000, 2_000, 3_000]
    assert [c.source for c in mkr] == ["mkr", "mkr", "mkr"]
    merged = merge_klines(mkr, sky, "sky")
    assert [c.open_time for c in merged] == [1_000, 2_000, 3_000, 4_000]
    assert merged[-1].close == 1.01
    assert merged[0].close == 24000 / 24000
    assert calls
