import os
import streamlit as st
from openai import OpenAI

# =========================
# 🔑 SAFE KEY LOADER
# =========================
API_KEY = (
    os.getenv("OPENROUTER_API_KEY")
    or st.secrets.get("OPENROUTER_API_KEY", None)
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

PRIMARY_MODEL = "openai/gpt-4o-mini"
FALLBACK_MODEL = "mistralai/mistral-7b-instruct"


def ask_gpt(prompt: str):

    if not API_KEY:
        return "❌ OPENROUTER_API_KEY missing (Streamlit Secrets or env)"

    # =========================
    # PRIMARY MODEL
    # =========================
    try:
        response = client.chat.completions.create(
            model=PRIMARY_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a PhD-level Turkic literature and poetry analyst."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content

    except Exception as e:

        # =========================
        # FALLBACK MODEL
        # =========================
        try:
            response = client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a fallback academic assistant."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return response.choices[0].message.content

        except Exception as e2:
            return f"❌ BOTH MODELS FAILED:\n{str(e2)}"
