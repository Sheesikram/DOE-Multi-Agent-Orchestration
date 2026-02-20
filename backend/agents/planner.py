from agents.base import run_llm

async def planner_node(state):
    prompt = f"""
Create a structured blog outline for:

Topic: {state['user_input']}

Requirements:
- Clear title
- 5–7 sections
- Bullet points under each section
- Specific to topic
"""

    state["plan"] = await run_llm(
        "You are an expert content strategist.",
        prompt,
        openai_key=state.get("openai_key")
    )

    return state
