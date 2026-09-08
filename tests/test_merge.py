from __future__ import annotations

import pytest

from mkr_sky.merge import convert_mkr_candle, convert_sky_candle, merge_klines, splice_quality
from mkr_sky.models import Candle


def _c(t: int, o: float, h: float, l: float, c: float, v: float, src: str) -> Candle:
    return Candle(
        open_time=t,
        open=o,
        high=h,
        low=l,
        close=c,
        volume=v,
        quote_volume=v * ((o + c) / 2),
        close_time=t + 86_399_999,
        source=src,
    )


def test_convert_mkr_to_sky_divides_price_and_scales_volume():
    mkr = _c(1, 24_000, 48_000, 12_000, 36_000, 2.0, "mkr")
    sky = convert_mkr_candle(mkr, "sky")
    assert sky.open == 1.0
    assert sky.high == 2.0
    assert sky.low == 0.5
    assert sky.close == 1.5
    assert sky.volume == 48_000.0
    assert sky.quote_volume == mkr.quote_volume
    assert sky.source == "mkr"


def test_convert_sky_to_mkr_multiplies_price():
    sky = _c(1, 0.08, 0.09, 0.07, 0.085, 24_000.0, "sky")
    mkr = convert_sky_candle(sky, "mkr")
    assert mkr.open == 1920.0
    assert mkr.high == 2160.0
    assert mkr.low == pytest.approx(1680.0)
    assert mkr.close == pytest.approx(2040.0)
    assert mkr.volume == pytest.approx(1.0)
    assert mkr.source == "sky"


def test_same_denomination_is_identity_for_prices():
    mkr = _c(1, 1800, 1810, 1790, 1805, 3, "mkr")
    assert convert_mkr_candle(mkr, "mkr").close == 1805
    sky = _c(1, 0.07, 0.08, 0.06, 0.075, 10, "sky")
    assert convert_sky_candle(sky, "sky").close == 0.075


def test_merge_appends_sky_after_mkr_history():
    mkr = [_c(1, 2400, 2500, 2300, 2450, 1, "mkr"), _c(2, 2450, 2600, 2400, 2500, 1, "mkr")]
    sky = [_c(3, 0.10, 0.11, 0.09, 0.105, 1000, "sky"), _c(4, 0.105, 0.12, 0.10, 0.11, 1000, "sky")]
    merged = merge_klines(mkr, sky, "sky")
    assert [c.open_time for c in merged] == [1, 2, 3, 4]
    assert [c.source for c in merged] == ["mkr", "mkr", "sky", "sky"]
    assert merged[0].close == 2450 / 24_000
    assert merged[3].close == 0.11


def test_overlap_uses_mkr_open_and_sky_close():
    mkr = [_c(10, 1800, 1900, 1700, 1813.7, 5, "mkr")]
    sky = [_c(10, 0.07558, 0.08, 0.07, 0.0695, 100_000, "sky")]
    merged = merge_klines(mkr, sky, "sky")
    assert len(merged) == 1
    bar = merged[0]
    assert bar.source == "splice"
    assert bar.open == 1800 / 24_000
    assert bar.close == 0.0695
    assert bar.high == max(1900 / 24_000, 0.08)
    assert bar.low == min(1700 / 24_000, 0.07)
    assert bar.volume == 5 * 24_000 + 100_000


def test_mkr_denomination_scales_sky_forward():
    mkr = [_c(1, 1800, 1810, 1790, 1800, 1, "mkr")]
    sky = [_c(2, 0.075, 0.08, 0.07, 0.076, 24_000, "sky")]
    merged = merge_klines(mkr, sky, "mkr")
    assert merged[0].close == 1800
    assert merged[1].close == 0.076 * 24_000
    assert merged[1].volume == 1.0


def test_binance_handoff_error_is_sub_basis_point():
    """Last MKR daily close vs first SKY daily open on Binance, 2025-09."""
    mkr = [_c(1_757_491_200_000, 1797.6, 1814.0, 1790.0, 1813.7, 208.5, "mkr")]
    sky = [_c(1_758_067_200_000, 0.07558, 0.08, 0.07, 0.07688, 4.86e8, "sky")]
    q = splice_quality(mkr, sky)
    assert q["abs_error"] < 1e-5
    assert q["rel_error"] < 2e-4


def test_merge_rejects_bad_denomination():
    try:
        merge_klines([], [], "usd")  # type: ignore[arg-type]
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "denomination" in str(exc)
