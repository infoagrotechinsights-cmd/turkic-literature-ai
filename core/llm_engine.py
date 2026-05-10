import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def ask_gpt(prompt):

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "Academic Turkic literature AI"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
