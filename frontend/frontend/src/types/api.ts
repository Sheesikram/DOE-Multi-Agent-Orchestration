export interface ChatRequest {
  message: string;
  openai_key?: string;
  tavily_key?: string;
}

export interface ExecutionStep {
  agent: string;
  iteration: number;
  status: "started" | "completed";
}

export interface ChatResponse {
  plan?: string;
  research?: string;
  draft?: string;
  critique?: {
    feedback: string;
    approved: boolean;
  };
  approved?: boolean;
  final?: string;

  // 🔥 execution metadata
  current_agent?: string;
  trace?: ExecutionStep[];
}
