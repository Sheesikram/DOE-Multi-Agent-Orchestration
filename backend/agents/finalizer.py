"""Finalizer agent implementation."""
from agents.base import run_llm

async def finalizer_node(state):
    state["final"] = state.get("draft")
    return state
