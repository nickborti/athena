from src.data.candle import Candle
from src.strategy.signal import Signal


def generate_signal(
    previous_candle: Candle,
    current_candle: Candle,
) -> Signal:
    if current_candle.close > previous_candle.close:
        return Signal(
            action="BUY",
            timestamp=current_candle.timestamp,
        )

    if current_candle.close < previous_candle.close:
        return Signal(
            action="SELL",
            timestamp=current_candle.timestamp,
        )

    return Signal(
        action="HOLD",
        timestamp=current_candle.timestamp,
    )