from agents.base import run_llm

async def writer_node(state):
    feedback = ""
    
    if state.get("critique") and not state.get("approved"):
        feedback = f"""
Improve the draft based on this feedback:
{state['critique']['feedback']}
"""

    prompt = f"""
Write a professional, detailed blog article based strictly on this outline:

{state['plan']}

Incorporate these research notes:

{state.get('research')}

{feedback}

Make it:
- Structured
- Clear
- Insightful
- Around 800-1200 words
"""
    state["draft"] = await run_llm(
        "You are a professional technology writer.",
        prompt,
        openai_key=state.get("openai_key")
    )
    return state
