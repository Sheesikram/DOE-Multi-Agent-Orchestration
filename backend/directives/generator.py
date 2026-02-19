"""Directive generator implementation."""

import json
from agents.base import run_llm
from directives.schema import Directive

DIRECTIVE_PROMPT = """
You are a directive planner.

Available agents:
- planner
- researcher
- critic
- writer
- finalizer

Return JSON only:

{
  "steps": [
    {"id": 1, "agent": "..."}
  ],
  "rules": {
    "retry_if_not_approved": true,
    "max_iterations": 2
  }
}
"""

async def generate_directive(user_input: str) -> Directive:
    raw = await run_llm(DIRECTIVE_PROMPT, user_input)
    parsed = json.loads(raw)
    return Directive(**parsed)
