type SignalInfo = {
  status: string;
  message: string;
};

const signal: SignalInfo = {
  status: "IDLE",
  message: "No active setup",
};

export default function SignalPanel() {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-6">
      <p className="text-xl font-semibold">Signal Engine</p>
      <p className="mt-2 text-sm text-zinc-400">{signal.status}</p>
      <p className="mt-6 text-2xl font-semibold">
        {signal.status === "IDLE" ? "—" : "SIGNAL"}
      </p>
      <p className="mt-4 text-sm text-zinc-500">{signal.message}</p>
      <p className="mt-6 text-sm font-medium text-zinc-500">STATUS: IDLE</p>
    </div>
  );
}
