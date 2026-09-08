from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping


@dataclass(frozen=True, slots=True)
class Candle:
    open_time: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    quote_volume: float
    close_time: int
    source: str

    def to_api(self) -> dict[str, Any]:
        return {
            "t": self.open_time,
            "o": self.open,
            "h": self.high,
            "l": self.low,
            "c": self.close,
            "v": self.volume,
            "qv": self.quote_volume,
            "ct": self.close_time,
            "src": self.source,
        }

    def to_csv_row(self) -> dict[str, Any]:
        row = asdict(self)
        return row


def candle_from_binance(row: Iterable[Any], source: str) -> Candle:
    open_time, open_, high, low, close, volume, close_time, quote_volume, *_ = row
    return Candle(
        open_time=int(open_time),
        open=float(open_),
        high=float(high),
        low=float(low),
        close=float(close),
        volume=float(volume),
        quote_volume=float(quote_volume),
        close_time=int(close_time),
        source=source,
    )


def candle_from_mapping(row: Mapping[str, Any]) -> Candle:
    return Candle(
        open_time=int(row["open_time"]),
        open=float(row["open"]),
        high=float(row["high"]),
        low=float(row["low"]),
        close=float(row["close"]),
        volume=float(row["volume"]),
        quote_volume=float(row["quote_volume"]),
        close_time=int(row["close_time"]),
        source=str(row["source"]),
    )
