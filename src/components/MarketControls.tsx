type MarketControlsProps = {
  onToggle: () => void;
};

export default function MarketControls({ onToggle }: MarketControlsProps) {
  return (
    <button
      className="rounded bg-blue-600 px-3 py-2 text white"
      onClick={onToggle}
    >
      Toggle Market
    </button>
  );
}
