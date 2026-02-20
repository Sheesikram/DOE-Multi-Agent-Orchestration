from tools.search import search_web

async def execute_tool(tool_name: str, arguments: dict, tavily_key: str = None):
    print(f"\n🔥 TOOL CALLED: {tool_name}")
    print(f"Arguments: {arguments}\n")

    if tool_name == "search_web":
        return await search_web(arguments["query"], tavily_key=tavily_key)

    raise ValueError(f"Unknown tool: {tool_name}")
