import DashboardHeader from "@/components/DasboardHeader";
import MarketOverview from "@/components/MarketOverview";
import MarketChart from "@/components/MarketChart";
import SignalPanel from "@/components/SignalPanel";
import DashboardControls from "@/components/DashboardControls";

export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white-p8">
      <section className="mx-auto-max-w-5xl">
        <DashboardHeader />
        <MarketOverview />
        <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-3">
          <MarketChart className="lg:col-span-2" />
          <SignalPanel />
        </div>

        <DashboardControls />
      </section>
    </main>
  );
}
