import type { Message } from "../types/message";

interface Props {
  message: Message;
}

export default function MessageBubble({ message }: Props) {
  const isUser = message.role === "user";

  return (
    <div
      style={{
        alignSelf: isUser ? "flex-end" : "flex-start",
        backgroundColor: isUser ? "#2563eb" : "#334155",
        color: "#f8fafc",
        padding: "14px 16px",
        borderRadius: "12px",
        maxWidth: "75%",
        marginBottom: "12px",
        whiteSpace: "pre-wrap",
        lineHeight: 1.5,
        fontSize: "15px",
      }}
    >
      {message.content}
    </div>
  );
}
