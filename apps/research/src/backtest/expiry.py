from datetime import datetime, timedelta

from src.data.candle import Candle


def find_expiry_candle(
    candles: list[Candle],
    signal_timestamp: datetime,
    expiry_minutes: int,
) -> Candle:
    if expiry_minutes not in (3, 5):
        raise ValueError("expiry_minutes must be 3 or 5")

    expiry_timestamp = signal_timestamp + timedelta(minutes=expiry_minutes)

    for candle in candles:
        if candle.timestamp == expiry_timestamp:
            return candle

    raise ValueError(
        f"No candle found at expiry timestamp {expiry_timestamp}"
    )