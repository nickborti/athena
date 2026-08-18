type MarketChartProps = {
  className?: string;
};

export default function MarketChart({ className }: MarketChartProps) {
  return (
    <div
      className={`rounded-xl border border-zinc-800 bg-zinc-900 p-6 ${className ?? ""}`}
    >
      <p className="text-xl font-semibold">Market Chart</p>
      <p className="text-sm text-zinc-500">Chart will appear here</p>
    </div>
  );
}
