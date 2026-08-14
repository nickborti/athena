type StatusCardProps = {
  label: string;
  value: string;
  color?: string;
};

export default function StatusCard({ label, value, color }: StatusCardProps) {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-800 p-5 text-white">
      <div className="text-sm text-zinc-400">{label}</div>
      <div className={`text-xl fontsemibold ${color}`}>{value}</div>
    </div>
  );
}
