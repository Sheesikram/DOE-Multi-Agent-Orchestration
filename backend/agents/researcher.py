from agents.base import run_llm
from mcp.executor import run_with_tools  # <-- add this line

async def researcher_node(state):
    messages = [
        {
            "role": "system",
            "content": """
You are a professional research agent.

You have access to a real-time web search tool called 'search_web'.

Use the search_web tool whenever:
- Up-to-date information is required
- Statistics or recent data is needed
- Factual verification is necessary

Do not hallucinate facts.
Prefer using the tool when uncertain.
"""
        },
        {
            "role": "user",
            "content": f"""
Research deeply about:

{state['plan']}

Provide structured research notes.
"""
        }
    ]

    state["research"] = await run_with_tools(messages)
    return state