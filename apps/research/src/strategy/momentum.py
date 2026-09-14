from src.data.candle import Candle
from src.strategy.signal import Signal


def generate_momentum_signal(
    previous_candle: Candle,
    current_candle: Candle,
) -> Signal:
    if (
        current_candle.close > current_candle.open
        and current_candle.close > previous_candle.high
    ):
        return Signal(
            action="BUY",
            timestamp=current_candle.timestamp,
        )

    if (
        current_candle.close < current_candle.open
        and current_candle.close < previous_candle.low
    ):
        return Signal(
            action="SELL",
            timestamp=current_candle.timestamp,
        )

    return Signal(
        action="HOLD",
        timestamp=current_candle.timestamp,
    )