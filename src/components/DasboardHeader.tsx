export default function DashboardHeader() {
  return (
    <header>
      <div className="mb-8 flex items-center justify-between border-b border-zinc-800 pb-6">
        <div>
          <h1 className="text-4xl font-bold">Axiom</h1>
          <p className="mt-2 text-zinc-400">Trading Intelligence</p>
        </div>
        <div className="flex flex-col items-end gap-1">
          <p className="text-lg font-semibold">EUR/USD</p>
          <p className="text-sm text-emerald-400">● LIVE</p>
        </div>
      </div>
    </header>
  );
}
