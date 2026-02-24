import type { ChatRequest, ChatResponse } from "./types/api";

interface ApiKeys {
  openaiKey?: string;
  tavilyKey?: string;
}

// Uses environment variable in production,
// falls back to localhost in development
const API_URL =
  import.meta.env.VITE_API_URL || "https://doe-multi-agent-orchestration.onrender.com";

export async function sendMessage(
  message: string,
  keys?: ApiKeys
): Promise<ChatResponse> {
  const payload: ChatRequest = {
    message,
    openai_key: keys?.openaiKey,
    tavily_key: keys?.tavilyKey,
  };

  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(
      `Server error (${response.status}): ${errorText}`
    );
  }

  const data: ChatResponse = await response.json();
  return data;
}