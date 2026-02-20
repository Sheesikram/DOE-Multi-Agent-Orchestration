import re
import json
from agents.base import run_llm

def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError("No valid JSON found")

async def critic_node(state):
    prompt = f"""
You are a strict reviewer.

Respond ONLY with valid JSON.
No explanations.
No markdown.
No text outside JSON.

Format:
{{
  "feedback": "string",
  "approved": true or false
}}

Draft:
{state.get("draft")}
"""

    raw = await run_llm(
        "You are a strict reviewer.",
        prompt,
        openai_key=state.get("openai_key")
    )

    state["critique"] = extract_json(raw)
    state["approved"] = state["critique"]["approved"]

    return state
