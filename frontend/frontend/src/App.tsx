import { useState, useRef, useEffect } from "react";
import { sendMessage } from "./api";
import MessageBubble from "./components/MessageBubble";
import ChatInput from "./components/ChatInput";
import ApiKeySettings from "./components/ApiKeySettings";
import type { Message } from "./types/message";

interface ExecutionStep {
  agent: string;
  iteration: number;
  status: "started" | "completed";
}

interface ApiKeys {
  openaiKey: string;
  tavilyKey: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [trace, setTrace] = useState<ExecutionStep[]>([]);
  const [apiKeys, setApiKeys] = useState<ApiKeys>({ openaiKey: "", tavilyKey: "" });
  const bottomRef = useRef<HTMLDivElement | null>(null);

  const handleSend = async (text: string) => {
    if (!apiKeys.openaiKey || !apiKeys.tavilyKey) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "⚠️ Please set your API keys first." },
      ]);
      return;
    }

    const userMessage: Message = { role: "user", content: text };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);
    setTrace([]); // reset trace for new request

    try {
      const data = await sendMessage(text, apiKeys);

      setTrace(data.trace || []);

      const assistantMessage: Message = {
        role: "assistant",
        content: data.draft || data.final || "No response returned.",
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Error connecting to server." },
      ]);
    }

    setLoading(false);
  };

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div style={styles.app}>
      <div style={styles.container}>
        <h1 style={styles.title}>AI Research Engine</h1>

        {/* 🔑 API Key Settings */}
        <ApiKeySettings onKeysChange={setApiKeys} />

        {/* 🔥 Execution Panel */}
        {trace.length > 0 && (
          <div style={styles.pipelineBox}>
            <h3 style={{ marginBottom: "10px" }}>Execution Pipeline</h3>

            {trace.map((step, index) => (
              <div key={index} style={styles.pipelineRow}>
                <span style={styles.agentName}>
                  {step.agent} (iteration {step.iteration})
                </span>

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
        )}

        {/* 💬 Chat */}
        <div style={styles.chatBox}>
          {messages.map((msg, index) => (
            <MessageBubble key={index} message={msg} />
          ))}

          {loading && (
            <div style={styles.loading}>
              Executing agents...
            </div>
          )}

          <div ref={bottomRef} />
        </div>

        <ChatInput onSend={handleSend} loading={loading} />
      </div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  app: {
    backgroundColor: "#0f172a",
    minHeight: "100vh",
    padding: "40px 20px",
    fontFamily: "Inter, system-ui, sans-serif",
    color: "#f8fafc",
  },
  container: {
    maxWidth: "900px",
    margin: "0 auto",
  },
  title: {
    fontSize: "2rem",
    marginBottom: "20px",
    textAlign: "center",
  },
  pipelineBox: {
    border: "1px solid #334155",
    borderRadius: "12px",
    padding: "16px",
    marginBottom: "20px",
    backgroundColor: "#1e293b",
  },
  pipelineRow: {
    display: "flex",
    justifyContent: "space-between",
    marginBottom: "6px",
    fontSize: "14px",
  },
  agentName: {
    fontWeight: 500,
    textTransform: "capitalize",
  },
  chatBox: {
    border: "1px solid #334155",
    borderRadius: "12px",
    padding: "20px",
    height: "500px",
    overflowY: "auto",
    marginBottom: "20px",
    backgroundColor: "#1e293b",
    display: "flex",
    flexDirection: "column",
  },
  loading: {
    color: "#94a3b8",
    fontStyle: "italic",
    padding: "10px",
  },
};

export default App;
