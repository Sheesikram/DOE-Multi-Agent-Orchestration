import { useState } from "react";

interface Props {
  onSend: (message: string) => void;
  loading: boolean;
}

export default function ChatInput({ onSend, loading }: Props) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  return (
    <div style={{ display: "flex", gap: "10px" }}>
      <input
        style={{
          flex: 1,
          padding: "14px",
          borderRadius: "8px",
          border: "1px solid #334155",
          backgroundColor: "#1e293b",
          color: "#f8fafc",
          outline: "none",
        }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask something..."
        disabled={loading}
      />
      <button
        onClick={handleSend}
        disabled={loading}
        style={{
          padding: "14px 20px",
          borderRadius: "8px",
          border: "none",
          backgroundColor: "#2563eb",
          color: "white",
          cursor: "pointer",
          opacity: loading ? 0.7 : 1,
        }}
      >
        {loading ? "..." : "Send"}
      </button>
    </div>
  );
}
