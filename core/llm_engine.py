import os
import streamlit as st
from openai import OpenAI

# =========================
# 🔑 FORCE KEY RESOLUTION
# =========================
def get_api_key():

    # 1. Streamlit secrets
    if hasattr(st, "secrets") and "OPENROUTER_API_KEY" in st.secrets:
        return st.secrets["OPENROUTER_API_KEY"]

    # 2. ENV
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key

    return None


API_KEY = get_api_key()

# 🚨 DEBUG (çok önemli)
if API_KEY:
    print("✅ API KEY LOADED")
else:
    print("❌ API KEY MISSING")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

PRIMARY_MODEL = "mistralai/mistral-7b-instruct"
FALLBACK_MODEL = "meta-llama/llama-3.1-8b-instruct"


def ask_gpt(prompt):

    if not API_KEY:
        return "❌ API KEY NOT FOUND (Secrets veya ENV kontrol et)"

    try:
        res = client.chat.completions.create(
            model=PRIMARY_MODEL,
            messages=[
                {"role": "system", "content": "You are a Turkic literature PhD assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return res.choices[0].message.content

    except Exception as e:

        try:
            res = client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=[
                    {"role": "system", "content": "Fallback academic assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return res.choices[0].message.content

        except Exception as e2:
            return f"❌ BOTH FAILED:\n{str(e2)}"
