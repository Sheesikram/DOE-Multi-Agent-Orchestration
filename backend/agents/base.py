from openai import AsyncOpenAI
from config import OPENAI_API_KEY, MODEL

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def run_llm(system_prompt: str, user_prompt: str):
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
