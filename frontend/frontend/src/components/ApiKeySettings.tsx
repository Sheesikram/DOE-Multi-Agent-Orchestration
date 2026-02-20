import { useState, useEffect } from "react";

interface Props {
  onKeysChange: (keys: { openaiKey: string; tavilyKey: string }) => void;
}

export default function ApiKeySettings({ onKeysChange }: Props) {
  const [openaiKey, setOpenaiKey] = useState("");
  const [tavilyKey, setTavilyKey] = useState("");
  const [isOpen, setIsOpen] = useState(false);

  // Load from localStorage on mount
  useEffect(() => {
    const savedOpenai = localStorage.getItem("openai_key") || "";
    const savedTavily = localStorage.getItem("tavily_key") || "";
    setOpenaiKey(savedOpenai);
    setTavilyKey(savedTavily);
    onKeysChange({ openaiKey: savedOpenai, tavilyKey: savedTavily });
  }, []);

  const handleSave = () => {
    if (!openaiKey.startsWith("sk-")) {
      alert("Invalid OpenAI key format.");
      return;
    }

    if (!tavilyKey.startsWith("tvly-")) {
      alert("Invalid Tavily key format.");
      return;
    }

    localStorage.setItem("openai_key", openaiKey);
    localStorage.setItem("tavily_key", tavilyKey);
    onKeysChange({ openaiKey, tavilyKey });
    setIsOpen(false);
  };

  const hasKeys = openaiKey && tavilyKey;

  return (
    <div style={styles.wrapper}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        style={{
          ...styles.toggleBtn,
          backgroundColor: hasKeys ? "#22c55e" : "#ef4444",
        }}
      >
        {hasKeys ? "✓ API Keys Set" : "⚠ Set API Keys"}
      </button>

      {isOpen && (
        <div style={styles.panel}>
          <h3 style={styles.heading}>API Configuration</h3>

          <label style={styles.label}>OpenAI API Key</label>
          <input
            type="password"
            value={openaiKey}
            onChange={(e) => setOpenaiKey(e.target.value)}
            placeholder="sk-..."
            style={styles.input}
          />

          <label style={styles.label}>Tavily API Key</label>
          <input
            type="password"
            value={tavilyKey}
            onChange={(e) => setTavilyKey(e.target.value)}
            placeholder="tvly-..."
            style={styles.input}
          />

          <button onClick={handleSave} style={styles.saveBtn}>
            Save Keys
          </button>

          <button
            onClick={() => {
              localStorage.removeItem("openai_key");
              localStorage.removeItem("tavily_key");
              setOpenaiKey("");
              setTavilyKey("");
              onKeysChange({ openaiKey: "", tavilyKey: "" });
            }}
            style={styles.clearBtn}
          >
            Clear Keys
          </button>

          <p style={styles.note}>
            Keys are stored locally in your browser and sent with each request.
          </p>
        </div>
      )}
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  wrapper: {
    marginBottom: "20px",
  },
  toggleBtn: {
    padding: "10px 20px",
    border: "none",
    borderRadius: "8px",
    color: "#fff",
    cursor: "pointer",
    fontWeight: 500,
    fontSize: "14px",
  },
  panel: {
    marginTop: "12px",
    padding: "20px",
    backgroundColor: "#1e293b",
    borderRadius: "12px",
    border: "1px solid #334155",
  },
  heading: {
    marginTop: 0,
    marginBottom: "16px",
    fontSize: "16px",
  },
  label: {
    display: "block",
    marginBottom: "6px",
    fontSize: "13px",
    color: "#94a3b8",
  },
  input: {
    width: "100%",
    padding: "10px 12px",
    marginBottom: "12px",
    backgroundColor: "#0f172a",
    border: "1px solid #334155",
    borderRadius: "6px",
    color: "#f8fafc",
    fontSize: "14px",
    boxSizing: "border-box",
  },
  saveBtn: {
    padding: "10px 20px",
    backgroundColor: "#3b82f6",
    border: "none",
    borderRadius: "6px",
    color: "#fff",
    cursor: "pointer",
    fontWeight: 500,
    width: "100%",
  },
  clearBtn: {
    padding: "10px 20px",
    backgroundColor: "#ef4444",
    border: "none",
    borderRadius: "6px",
    color: "#fff",
    cursor: "pointer",
    fontWeight: 500,
    width: "100%",
    marginTop: "8px",
  },
  note: {
    marginTop: "12px",
    fontSize: "12px",
    color: "#64748b",
    textAlign: "center",
  },
};

