"""Execution store for managing agent execution state."""

import uuid

EXECUTIONS = {}

def create_execution(state):
    execution_id = str(uuid.uuid4())
    EXECUTIONS[execution_id] = state
    return execution_id

def update_execution(execution_id, state):
    EXECUTIONS[execution_id] = state
