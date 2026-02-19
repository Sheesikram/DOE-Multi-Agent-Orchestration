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

    raw = await run_llm("You are a strict reviewer.", prompt)

    state["critique"] = extract_json(raw)
    state["approved"] = state["critique"]["approved"]

    return state




async def writer_node(state):
    feedback = ""
    
    if state.get("critique") and not state.get("approved"):
        feedback = f"""
Improve the draft based on this feedback:
{state['critique']['feedback']}
"""

    prompt = f"""
Write a professional, detailed blog based on:

Outline:
{state['plan']}

Research:
{state['research']}

{feedback}

Ensure improvements are applied.
"""

    state["draft"] = await run_llm(
        "You are a professional technology writer.",
        prompt
    )

    return state
