import type { ChatRequest, ChatResponse } from "./types/api";

const API_URL = "http://127.0.0.1:8000/chat";

interface ApiKeys {
  openaiKey?: string;
  tavilyKey?: string;
}

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
