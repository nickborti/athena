from src.backtest.summary import BacktestSummary


class ExpiryComparison:
    def __init__(
        self,
        summary_3m: BacktestSummary,
        summary_5m: BacktestSummary,
    ) -> None:
        self.summary_3m = summary_3m
        self.summary_5m = summary_5m

        if summary_3m.win_rate > summary_5m.win_rate:
            self.better_expiry = 3
        elif summary_5m.win_rate > summary_3m.win_rate:
            self.better_expiry = 5
        else:
            self.better_expiry = None