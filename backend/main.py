"""Main entry point for the multi-agent system."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from directives.executor import execute_directive
from directives.schema import Directive, DirectiveStep, DirectiveRules

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def chat(data: dict):
    try:
        user_input = data.get("message")

        if not user_input:
            raise HTTPException(status_code=400, detail="Message is required")

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
            "plan": final_state.get("plan"),
            "research": final_state.get("research"),
            "draft": final_state.get("draft"),
            "critique": final_state.get("critique"),
            "approved": final_state.get("approved"),
            "final": final_state.get("final"),

            # 🔥 NEW — Execution metadata
            "current_agent": final_state.get("current_agent"),
            "trace": final_state.get("trace", []),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
