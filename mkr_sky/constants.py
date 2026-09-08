"""Official MKR→SKY redenomination constants.

MakerDAO / Sky protocol converts 1 MKR into 24,000 SKY. Binance completed the
spot swap by delisting MKRUSDT at 2025-09-15 03:00 UTC and listing SKYUSDT at
2025-09-17 08:00 UTC. Daily SKY bars start at 2025-09-17 00:00 UTC.
"""

from __future__ import annotations

RATIO = 24_000
RATIO_F = float(RATIO)

# First SKY daily bar on Binance (UTC). Intraday series start later the same day
# (08:00 UTC); callers should prefer the first live SKY candle when available.
CUTOVER_MS = 1_758_067_200_000  # 2025-09-17 00:00:00 UTC

MKR_SYMBOL = "MKRUSDT"
SKY_SYMBOL = "SKYUSDT"

BINANCE_KLINES_URL = "https://data-api.binance.vision/api/v3/klines"
BINANCE_FALLBACK_URL = "https://api.binance.com/api/v3/klines"

SUPPORTED_INTERVALS = ("1h", "4h", "1d", "1w", "1M")
DENOMINATIONS = ("sky", "mkr")

INTERVAL_MS = {
    "1h": 3_600_000,
    "4h": 14_400_000,
    "1d": 86_400_000,
    "1w": 7 * 86_400_000,
    "1M": 30 * 86_400_000,
}
