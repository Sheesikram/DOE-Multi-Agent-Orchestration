import json
from openai import AsyncOpenAI
from config import OPENAI_API_KEY, MODEL
from mcp.tools import TOOLS
from mcp.router import execute_tool

async def run_with_tools(messages, openai_key: str = None, tavily_key: str = None):
    # Use provided key or fall back to config
    api_key = openai_key or OPENAI_API_KEY
    client = AsyncOpenAI(api_key=api_key)
    
    response = await client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if not message.tool_calls:
        return message.content

    # 🔒 LIMIT TOOL CALLS TO 1
    tool_call = message.tool_calls[0]

    messages.append({
        "role": "assistant",
        "content": message.content,
        "tool_calls": [tool_call]
    })

    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    # Pass tavily_key to tool execution
    tool_result = await execute_tool(tool_name, arguments, tavily_key=tavily_key)

    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": tool_result
    })

    second_response = await client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return second_response.choices[0].message.content
