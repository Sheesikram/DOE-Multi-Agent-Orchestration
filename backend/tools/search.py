import httpx
from config import TAVILY_API_KEY

async def search_web(query: str, tavily_key: str = None):
    # Use provided key or fall back to config
    api_key = tavily_key or TAVILY_API_KEY
    
    url = "https://api.tavily.com/search"

    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "advanced",
        "include_answer": True,
        "max_results": 5
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        data = response.json()

    results = data.get("results", [])

    formatted = ""

    for r in results:
        formatted += f"""
Title: {r.get("title")}
URL: {r.get("url")}
Content: {r.get("content")}
--------------------------------
"""

    return formatted.strip()
