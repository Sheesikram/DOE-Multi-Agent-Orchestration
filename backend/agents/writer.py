from agents.base import run_llm

async def writer_node(state):
    prompt = f"""
Write a professional, detailed blog article based strictly on this outline:

{state['plan']}

Incorporate these research notes:

{state.get('research')}

Make it:
- Structured
- Clear
- Insightful
- Around 800-1200 words
"""
    state["draft"] = await run_llm("You are a professional technology writer.", prompt)
    return state
