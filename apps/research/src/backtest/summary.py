class BacktestSummary:
    def __init__(
        self,
        results: list[str],
        expiry_minutes: int,
    ) -> None:
        if expiry_minutes not in (3, 5):
            raise ValueError("expiry_minutes must be 3 or 5")

        self.expiry_minutes = expiry_minutes
        self.total_trades = len(results)
        self.wins = results.count("WIN")
        self.losses = results.count("LOSS")
        self.ties = results.count("TIE")

        resolved_trades = self.wins + self.losses

        self.win_rate = (
            round((self.wins / resolved_trades) * 100, 2)
            if resolved_trades
            else 0.0
        )