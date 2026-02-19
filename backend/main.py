"""Main entry point for the multi-agent system."""

from fastapi import FastAPI
from directives.generator import generate_directive
from directives.executor import execute_directive
from directives.schema import Directive, DirectiveStep, DirectiveRules

app = FastAPI()

@app.post("/chat")
async def chat(data: dict):
    user_input = data["message"]

   # directive = await generate_directive(user_input)
    directive = Directive(
        steps=[
            DirectiveStep(id=1, agent="planner"),
            DirectiveStep(id=2, agent="researcher"),
            DirectiveStep(id=3, agent="writer"),
            DirectiveStep(id=4, agent="critic"),
            DirectiveStep(id=5, agent="finalizer"),
        ],
        rules=DirectiveRules(
            retry_if_not_approved=True,
            max_iterations=2
        )
    )
    final_state = await execute_directive(directive, user_input)

    return {
        "plan": final_state["plan"],
        "research": final_state["research"],
        "draft": final_state["draft"],
        "critique": final_state["critique"],
        "approved": final_state["approved"],
    }

