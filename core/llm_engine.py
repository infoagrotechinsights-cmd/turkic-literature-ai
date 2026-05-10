import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_gpt(prompt):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",  # OpenRouter formatı
        messages=[
            {"role": "system", "content": "You are an academic poetry analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
