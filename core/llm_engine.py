import streamlit as st
from openai import OpenAI

API_KEY = st.secrets.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

PRIMARY_MODEL = "meta-llama/llama-3.1-8b-instruct"
FALLBACK_MODEL = "openai/gpt-4o-mini"


def ask_gpt(prompt):

    if not API_KEY:
        return "❌ API KEY MISSING"

    try:
        response = client.chat.completions.create(
            model=PRIMARY_MODEL,
            messages=[
                {"role": "system", "content": "You are a Turkic literature PhD analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:

        try:
            response = client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=[
                    {"role": "system", "content": "Fallback academic assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content

        except Exception as e2:
            return f"❌ MODEL ERROR:\n{str(e2)}"
