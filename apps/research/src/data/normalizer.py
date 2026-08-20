from dataclasses import dataclass
from datetime import datetime, timedelta

from src.data.candle import Candle


@dataclass
class Gap:
    previous_timestamp: datetime
    next_timestamp: datetime


@dataclass
class NormalizedCandles:
    candles: list[Candle]
    gaps: list[Gap]

def timeframe_to_timedelta(timeframe: str) -> timedelta:
    if timeframe.endswith("m"):
        minutes = int(timeframe[:-1])
        return timedelta(minutes=minutes)

    if timeframe.endswith("h"):
        hours = int(timeframe[:-1])
        return timedelta(hours=hours)

    raise ValueError(f"Unsupported timeframe: {timeframe}")

def normalize_candles(candles: list[Candle], from_timestamp: datetime, to_timestamp: datetime):
    # normalized = sorted(candles, key=lambda candle: candle.timestamp)
    normalized = sorted(
            [
                candle
                for candle in candles
                if from_timestamp <= candle.timestamp <= to_timestamp
            ],
            key=lambda candle: candle.timestamp,
        )

    unique_candles = []
    seen_timestamps = set()

    for candle in normalized:
        if candle.timestamp not in seen_timestamps:
            unique_candles.append(candle)
            seen_timestamps.add(candle.timestamp)

    gaps = []

    for previous, current in zip(unique_candles, unique_candles[1:]):
        expected_interval = timeframe_to_timedelta(previous.timeframe)

        if current.timestamp - previous.timestamp > expected_interval:
                    gaps.append(
                        Gap(
                            previous_timestamp=previous.timestamp,
                            next_timestamp=current.timestamp,
                        )
                    )

    
    return NormalizedCandles(
        candles=unique_candles,
        gaps=gaps,
    )
    

    