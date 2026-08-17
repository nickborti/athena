"use client";

import { useState } from "react";
import StatusCard from "./StatusCard";
import MarketControls from "./MarketControls";

export default function DashboardControls() {
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
    <div className="mt-8 grid gap-4 md-grid-cols-3">
      {cards.map(({ label, value, color }) => {
        return (
          <StatusCard key={label} label={label} value={value} color={color} />
        );
      })}

      <MarketControls onToggle={toggleMarket} />
    </div>
  );
}
