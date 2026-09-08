from __future__ import annotations

from dataclasses import replace
from typing import Iterable, Literal, Sequence

from mkr_sky.constants import RATIO_F
from mkr_sky.models import Candle

Denomination = Literal["sky", "mkr"]


def convert_mkr_candle(candle: Candle, denomination: Denomination) -> Candle:
    """Express an MKR candle in the requested unit."""
    if denomination == "mkr":
        return replace(candle, source="mkr")
    return Candle(
        open_time=candle.open_time,
        open=candle.open / RATIO_F,
        high=candle.high / RATIO_F,
        low=candle.low / RATIO_F,
        close=candle.close / RATIO_F,
        volume=candle.volume * RATIO_F,
        quote_volume=candle.quote_volume,
        close_time=candle.close_time,
        source="mkr",
    )


def convert_sky_candle(candle: Candle, denomination: Denomination) -> Candle:
    """Express a SKY candle in the requested unit."""
    if denomination == "sky":
        return replace(candle, source="sky")
    return Candle(
        open_time=candle.open_time,
        open=candle.open * RATIO_F,
        high=candle.high * RATIO_F,
        low=candle.low * RATIO_F,
        close=candle.close * RATIO_F,
        volume=candle.volume / RATIO_F,
        quote_volume=candle.quote_volume,
        close_time=candle.close_time,
        source="sky",
    )


def splice_overlap(mkr_candle: Candle, sky_candle: Candle) -> Candle:
    """Join a period that traded as MKR first and SKY later.

    Open comes from MKR (the week/month started before the listing). Close
    comes from SKY (the current token). High/low span both prints. Volumes add.
    """
    if mkr_candle.open_time != sky_candle.open_time:
        raise ValueError("overlap candles must share open_time")
    return Candle(
        open_time=mkr_candle.open_time,
        open=mkr_candle.open,
        high=max(mkr_candle.high, sky_candle.high),
        low=min(mkr_candle.low, sky_candle.low),
        close=sky_candle.close,
        volume=mkr_candle.volume + sky_candle.volume,
        quote_volume=mkr_candle.quote_volume + sky_candle.quote_volume,
        close_time=max(mkr_candle.close_time, sky_candle.close_time),
        source="splice",
    )


def merge_klines(
    mkr: Sequence[Candle] | Iterable[Candle],
    sky: Sequence[Candle] | Iterable[Candle],
    denomination: Denomination = "sky",
) -> list[Candle]:
    """Build a continuous series: MKR history, then SKY, overlapping bars spliced."""
    if denomination not in ("sky", "mkr"):
        raise ValueError(f"unsupported denomination: {denomination}")

    converted_mkr = [convert_mkr_candle(c, denomination) for c in mkr]
    converted_sky = [convert_sky_candle(c, denomination) for c in sky]

    by_time: dict[int, Candle] = {}
    for candle in converted_mkr:
        by_time[candle.open_time] = candle
    for candle in converted_sky:
        existing = by_time.get(candle.open_time)
        if existing is None:
            by_time[candle.open_time] = candle
        else:
            by_time[candle.open_time] = splice_overlap(existing, candle)

    return sorted(by_time.values(), key=lambda c: c.open_time)


def splice_quality(mkr: Sequence[Candle], sky: Sequence[Candle]) -> dict[str, float | int | None]:
    """How tightly the last MKR print matches the first SKY print at 1:24,000."""
    if not mkr or not sky:
        return {
            "last_mkr_close": None,
            "first_sky_open": None,
            "mkr_as_sky": None,
            "abs_error": None,
            "rel_error": None,
            "last_mkr_open_time": None,
            "first_sky_open_time": None,
        }
    last_mkr = mkr[-1]
    first_sky = sky[0]
    mkr_as_sky = last_mkr.close / RATIO_F
    abs_error = abs(mkr_as_sky - first_sky.open)
    rel_error = abs_error / first_sky.open if first_sky.open else None
    return {
        "last_mkr_close": last_mkr.close,
        "first_sky_open": first_sky.open,
        "mkr_as_sky": mkr_as_sky,
        "abs_error": abs_error,
        "rel_error": rel_error,
        "last_mkr_open_time": last_mkr.open_time,
        "first_sky_open_time": first_sky.open_time,
    }
