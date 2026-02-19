import httpx
from config import TAVILY_API_KEY

async def search_web(query: str):
    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
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
