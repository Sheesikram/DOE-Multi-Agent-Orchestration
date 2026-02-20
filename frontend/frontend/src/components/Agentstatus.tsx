import type { ExecutionStep } from "../types/api";

interface Props {
  trace?: ExecutionStep[];
}

export default function AgentStatus({ trace }: Props) {
  if (!trace || trace.length === 0) return null;

  return (
    <div
      style={{
        background: "#1e293b",
        padding: "16px",
        borderRadius: "10px",
        marginBottom: "15px",
      }}
    >
      <h3 style={{ marginBottom: "10px" }}>Execution Pipeline</h3>

      {trace.map((step, index) => (
        <div key={index} style={{ marginBottom: "6px" }}>
          <span style={{ fontWeight: 500 }}>
            {step.agent}
          </span>
          {" — "}
          <span
            style={{
              color:
                step.status === "completed"
                  ? "#22c55e"
                  : "#facc15",
            }}
          >
            {step.status}
          </span>
        </div>
      ))}
    </div>
  );
}
