import httpx
from bs4 import BeautifulSoup

MAX_CONTENT_LENGTH = 20000  # limit response size

async def scrape_page(url: str):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)

        if response.status_code != 200:
            return {"error": "Failed to fetch page"}

        html = response.text[:MAX_CONTENT_LENGTH]

        soup = BeautifulSoup(html, "lxml")

        # Remove unwanted tags
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        cleaned_text = "\n".join(
            line.strip() for line in text.splitlines() if line.strip()
        )
        ALLOWED_DOMAINS = ["bbc.com", "reuters.com", "who.int", "gov", "edu"]

        return {
            "url": url,
            "content": cleaned_text[:10000]  # final limit
        }

    except Exception as e:
        return {"error": str(e)}