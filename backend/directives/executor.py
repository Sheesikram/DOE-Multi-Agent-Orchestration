"""Directive executor implementation."""

from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.critic import critic_node
from agents.writer import writer_node
from agents.finalizer import finalizer_node
from execution.store import create_execution, update_execution

AGENT_MAP = {
    "planner": planner_node,
    "researcher": researcher_node,
    "critic": critic_node,
    "writer": writer_node,
    "finalizer": finalizer_node,
}


async def execute_directive(directive, user_input,openai_key=None, tavily_key=None):
    state = {
        "user_input": user_input,
        "plan": None,
        "research": None,
        "draft": None,
        "critique": None,
        "approved": False,
        "openai_key": openai_key,
        "tavily_key": tavily_key,
        "final": None,
        "current_agent": None,
        "trace": [],
    }

    execution_id = create_execution(state)
    iteration = 0

    while iteration < directive.rules.max_iterations:

        for step in directive.steps:
            agent_name = step.agent
            agent_fn = AGENT_MAP.get(agent_name)

            if not agent_fn:
                raise Exception(f"Unknown agent: {agent_name}")

            # 🔥 Mark agent as started
            state["current_agent"] = agent_name
            state["trace"].append({
                "agent": agent_name,
                "iteration": iteration,
                "status": "started"
            })

            update_execution(execution_id, state)

            # Execute agent
            state = await agent_fn(state)

            # 🔥 Mark agent as completed
            state["trace"][-1]["status"] = "completed"

            update_execution(execution_id, state)

        # Retry logic
        if directive.rules.retry_if_not_approved and not state["approved"]:
            iteration += 1
            continue

        break

    # Clear current agent after execution
    state["current_agent"] = None

    update_execution(execution_id, state)

    return state

