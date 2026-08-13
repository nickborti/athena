import StatusCard from "@/components/StatusCard";

export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white-p8">
      <section className="mx-auto-max-w-5xl">
        <h1 className="text-4xl font-bold">Axiom</h1>
        <p className="mt-2 text-zinc-400">Trading Intelligence Dashboard</p>

        <div className="mt-8 grid gap-4 md-grid-cols-3">
          <StatusCard label={"Market Status"} value={"Open"} />
          <StatusCard label={"Strategy"} value={"Trend Following"} />
          <StatusCard label={"Engine Status"} value={"Ready"} />
        </div>
      </section>
    </main>
  );
}
