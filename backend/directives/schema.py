"""Schema definitions for directives."""

from pydantic import BaseModel, Field
from typing import List

class DirectiveStep(BaseModel):
    id: int
    agent: str

class DirectiveRules(BaseModel):
    retry_if_not_approved: bool = False
    max_iterations: int = Field(default=1, le=3)

class Directive(BaseModel):
    steps: List[DirectiveStep]
    rules: DirectiveRules
