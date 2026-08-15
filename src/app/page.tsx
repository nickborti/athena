"use client";
import StatusCard from "@/components/StatusCard";
import MarketControls from "@/components/MarketControls";
import { useState } from "react";
import DashboardHeader from "@/components/DasboardHeader";
import MarketOverview from "@/components/MarketOverview";

export default function Home() {
  const [marketOpen, setMarketOpen] = useState(true);
  const cards = [
    {
      label: "Market Status",
      value: marketOpen ? "Open" : "Closed",
      color: marketOpen ? "text-green-400" : "text-red-400",
    },
    { label: "Strategy", value: "Trend Following" },
    { label: "Engine Status", value: "Ready" },
    { label: "Risk Level", value: "Low" },
  ];

  const toggleMarket = () => {
    setMarketOpen(!marketOpen);
  };

  return (
    <main className="min-h-screen bg-zinc-950 text-white-p8">
      <section className="mx-auto-max-w-5xl">
        <DashboardHeader />
        <MarketOverview />

        <div className="mt-8 grid gap-4 md-grid-cols-3">
          {cards.map(({ label, value, color }) => {
            return (
              <StatusCard
                key={label}
                label={label}
                value={value}
                color={color}
              />
            );
          })}

          <MarketControls onToggle={toggleMarket} />
        </div>
      </section>
    </main>
  );
}
