import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

PRIMARY_MODEL = "openai/gpt-4o-mini"
FALLBACK_MODEL = "mistralai/mistral-7b-instruct"


def ask_gpt(prompt):

    if not os.getenv("OPENROUTER_API_KEY"):
        return "❌ API key missing"

    # 1. dene (primary model)
    try:
        response = client.chat.completions.create(
            model=PRIMARY_MODEL,
            messages=[
                {"role": "system", "content": "You are a PhD-level poetry analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:

        # 2. fallback model
        try:
            response = client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=[
                    {"role": "system", "content": "You are a backup academic assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content

        except Exception as e2:
            return f"❌ Both models failed: {str(e2)}"
