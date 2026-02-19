import json
from openai import AsyncOpenAI
from config import OPENAI_API_KEY, MODEL
from mcp.tools import TOOLS
from mcp.router import execute_tool

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def run_with_tools(messages):
    response = await client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # If no tools were called
    if not message.tool_calls:
        return message.content

    # Append the assistant message ONCE
    messages.append({
        "role": "assistant",
        "content": message.content,
        "tool_calls": message.tool_calls
    })

    # Execute each tool call
    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        tool_result = await execute_tool(tool_name, arguments)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": tool_result
        })

    # Call model again after ALL tool responses
    second_response = await client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return second_response.choices[0].message.content
