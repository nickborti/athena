export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white-p8">
      <section className="mx-auto-max-w-5xl">
        <h1 className="text-4xl font-bold">Axiom</h1>
        <p className="mt-2 text-zinc-400">Trading Intelligence Dashboard</p>

        <div className="mt-8 grid gap-4 md-grid-cols-3">
          <div className="rounded-xl border border-zinc-800 bg-zinc-800 p-5 text-white">
            <div className="text-sm text-zinc-400">Market Status</div>
            <div className="text-xl fontsemibold">Open</div>
          </div>
          <div className="rounded-xl border border-zinc-800 bg-zinc-800 p-5 text-white">
            <div className="text-sm text-zinc-400">Strategy</div>
            <div className="text-xl fontsemibold">Trend Following</div>
          </div>
          <div className="rounded-xl border border-zinc-800 bg-zinc-800 p-5 text-white">
            <div className="text-sm text-zinc-400">Engine Status</div>
            <div className="text-xl fontsemibold">Ready</div>
          </div>
        </div>
      </section>
    </main>
  );
}
