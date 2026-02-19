from agents.base import run_llm

async def researcher_node(state):
    prompt = f"""
Research deeply based on this outline:

{state['plan']}

Provide structured notes.
"""

    state["research"] = await run_llm("You are a researcher.", prompt)

    return state
