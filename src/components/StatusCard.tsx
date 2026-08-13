type StatusCardProps = {
  label: string;
  value: string;
};

export default function StatusCard({ label, value }: StatusCardProps) {
  return (
    <div className="rounded-xl border border-zinc-800 bg-zinc-800 p-5 text-white">
      <div className="text-sm text-zinc-400">{label}</div>
      <div className="text-xl fontsemibold">{value}</div>
    </div>
  );
}
