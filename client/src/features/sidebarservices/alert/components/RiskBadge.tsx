interface Props {
  risk: string;
}

export default function RiskBadge({ risk }: Props) {
  const styles =
    risk === "High"
      ? "bg-red-100 text-red-600"
      : risk === "Medium"
      ? "bg-yellow-100 text-yellow-600"
      : "bg-green-100 text-green-600";

  return <span className={`px-2 py-1 rounded ${styles}`}>{risk}</span>;
}
