type MarketMetric = {
  label: string;
  value: string | number;
};

type MarketData = {
  symbol: string;
  price: number;
  change: number;
  status: string;
};

export default async function MarketOverview() {
  const response = await fetch("http://localhost:3001/api/market", {
    cache: "no-store",
  });
  if (!response.ok) {
    throw new Error("Failed to fetch market data");
  }
  const market: MarketData = await response.json();

  const metrics: MarketMetric[] = [
    { label: "Price", value: market.price.toFixed(4) },
    {
      label: "Change",
      value: `${market.change > 0 ? `+${market.change.toFixed(2)}%` : `${market.change.toFixed(2)}%`}`,
    },
    { label: "Market Regime", value: "Trending" },
    { label: "Volatility", value: "Normal" },
  ];

  return (
    <section className="mt-8 rounded-xl border border-zinc-800 bg-zinc-900 p-6">
      <p className="text-xl font-semibold">Market Overview</p>
      <p className="mt-1 text-sm text-zinc-400">{market.symbol}</p>
      <div className="grid grid-cols-1 gap-6 md:grid-cols-4">
        {metrics.map((metric: MarketMetric) => {
          return (
            <div key={metric.label}>
              <p className="text-sm text-zinc-400">{metric.label}</p>
              <p className="text-xl font-semibold">{metric.value}</p>
            </div>
          );
        })}
        <p className="mt-4 text-sm text-zinc-400">
          Market status: {market.status}
        </p>
      </div>
    </section>
  );
}
