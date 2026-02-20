from agents.base import run_llm
from mcp.executor import run_with_tools

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


You may call the search_web tool only once.
Combine all necessary information into a single comprehensive query.
Be strategic and concise.

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

    state["research"] = await run_with_tools(
        messages,
        openai_key=state.get("openai_key"),
        tavily_key=state.get("tavily_key")
    )
    return state
