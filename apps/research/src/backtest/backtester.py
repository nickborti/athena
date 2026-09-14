from dataclasses import dataclass
from datetime import datetime
from src.strategy.signal import Signal


@dataclass
class BacktestResult:
    position: int
    entry_price: float | None
    timestamp: datetime


class Backtester:
    def process_signal(
        self,
        signal: Signal,
        price: float,
        timestamp: datetime,
    ) -> BacktestResult:
        if signal.action == "BUY":
            return BacktestResult(
                position=1,
                entry_price=price,
                timestamp=timestamp,
            )

        return BacktestResult(
            position=0,
            entry_price=None,
            timestamp=timestamp,
        )