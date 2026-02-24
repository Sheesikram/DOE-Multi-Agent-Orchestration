from tools.search import search_web
from tools.scrape import scrape_page

async def execute_tool(
    tool_name: str,
    arguments: dict,
    openai_key: str | None = None,
    tavily_key: str | None = None
):
    if tool_name == "search_web":
        return await search_web(arguments["query"])

    if tool_name == "scrape_page":
        return await scrape_page(arguments["url"])

    raise Exception(f"Unknown tool: {tool_name}")