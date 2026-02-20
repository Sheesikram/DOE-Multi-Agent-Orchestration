from openai import AsyncOpenAI
from config import OPENAI_API_KEY, MODEL

async def run_llm(system_prompt: str, user_prompt: str, openai_key: str = None):
    # Use provided key or fall back to config
    api_key = openai_key or OPENAI_API_KEY
    client = AsyncOpenAI(api_key=api_key)
    
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
