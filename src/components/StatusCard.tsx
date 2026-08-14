type StatusCardProps = {
  label: string;
  value: string;
  color?: string;
  onClick?: () => void;
};

export default function StatusCard({
  label,
  value,
  color,
  onClick,
}: StatusCardProps) {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-800 p-5 text-white">
      <div className="text-sm text-zinc-400">{label}</div>
      <div className={`text-xl fontsemibold ${color}`}>{value}</div>
      <button
        className="rounded bg-blue-600 px-3 py-2 text white"
        onClick={onClick}
      >
        Toggle
      </button>
    </div>
  );
}
