import streamlit as st
from openai import OpenAI
from core.prompt_engine import build_prompt

API_KEY = st.secrets.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

MODEL_PRIMARY = "meta-llama/llama-3.1-8b-instruct"
MODEL_FALLBACK = "openai/gpt-4o-mini"


def ask_gpt(poem, mode="academic"):

    if not API_KEY:
        return "❌ API KEY MISSING"

    prompt = build_prompt(poem, mode)

    try:
        res = client.chat.completions.create(
            model=MODEL_PRIMARY,
            messages=[
                {
                    "role": "system",
                    "content": "SADECE TÜRKÇE akademik analiz üret."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return res.choices[0].message.content

    except Exception:

        res = client.chat.completions.create(
            model=MODEL_FALLBACK,
            messages=[
                {
                    "role": "system",
                    "content": "Türkçe akademik analiz üret."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return res.choices[0].message.content
