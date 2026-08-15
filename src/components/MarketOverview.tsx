type MarketMetric = {
  label: string;
  value: string;
};

export default function MarketOverview() {
  const metrics: MarketMetric[] = [
    { label: "Price", value: "1.XXXX" },
    { label: "Change", value: "+0.25%" },
    { label: "Market Regime", value: "Trending" },
    { label: "Volatility", value: "Normal" },
  ];
  return (
    <section className="mt-8 rounded-xl border border-zinc-800 bg-zinc-900 p-6">
      <p className="text-xl font-semibold">Market Overview</p>
      <p className="mt-1 text-sm text-zinc-400">EUR/USD</p>
      <div className="grid grid-cols-1 gap-6 md:grid-cols-4">
        {metrics.map((metric: MarketMetric) => {
          return (
            <div key={metric.label}>
              <p className="text-sm text-zinc-400">{metric.label}</p>
              <p className="text-xl font-semibold">{metric.value}</p>
            </div>
          );
        })}
        {/* <div>
          <p className="text-sm text-zinc-400">Price</p>
          <p className="text-2xl font-semibold">1.XXXX</p>
        </div>
        <div>
          <p className="text-sm text-zinc-400">Change</p>
          <p className="text-xl font-semibold">+0.25%</p>
        </div>
        <div>
          <p className="text-sm text-zinc-400">Market Regime</p>
          <p className="text-xl font-semibold">Trending</p>
        </div>
        <div>
          <p className="text-sm text-zinc-400">Volatility</p>
          <p className="text-xl font-semibold">Normal</p>
        </div> */}
      </div>
    </section>
  );
}
