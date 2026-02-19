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

async def execute_directive(directive, user_input):
    state = {
        "user_input": user_input,
        "plan": None,
        "research": None,
        "draft": None,
        "critique": None,
        "approved": False,
        "final": None
    }

    execution_id = create_execution(state)
    iteration = 0

    while iteration < directive.rules.max_iterations:
        for step in directive.steps:
            agent_fn = AGENT_MAP.get(step.agent)
            if not agent_fn:
                raise Exception(f"Unknown agent: {step.agent}")

            state = await agent_fn(state)
            update_execution(execution_id, state)

        if directive.rules.retry_if_not_approved and not state["approved"]:
            iteration += 1
            continue

        break

    return state
