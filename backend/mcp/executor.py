import json
from openai import AsyncOpenAI
from config import OPENAI_API_KEY, MODEL
from mcp.tools import TOOLS
from mcp.router import execute_tool


async def run_with_tools(messages, openai_key: str = None, tavily_key: str = None):
    api_key = openai_key or OPENAI_API_KEY
    client = AsyncOpenAI(api_key=api_key)

    MAX_TOOL_CALLS = 3
    tool_call_count = 0

    while True:
        response = await client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message

        print("MODEL RESPONSE FINISH REASON:", response.choices[0].finish_reason)

        # ✅ If no tool call → final answer
        if not message.tool_calls:
            return message.content

        # 🔒 Safety guard
        tool_call_count += 1
        if tool_call_count > MAX_TOOL_CALLS:
            return "Error: Too many tool calls. Aborting."

        # Append assistant tool call message
        messages.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": message.tool_calls
        })

        # Only handle first tool call (safe + controlled)
        tool_call = message.tool_calls[0]

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"🔥 TOOL CALLED: {tool_name}")
        print(f"Arguments: {arguments}")

        # Execute tool
        tool_result = await execute_tool(
            tool_name,
            arguments,
            openai_key=openai_key,
            tavily_key=tavily_key
        )

        # Append tool result
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(tool_result)
        })

        # Loop continues → model will consume tool output and respond