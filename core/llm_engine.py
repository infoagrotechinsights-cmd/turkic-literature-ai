import streamlit as st
from openai import OpenAI

API_KEY = st.secrets.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

def ask_gpt(prompt):

    if not API_KEY:
        return "❌ API KEY NOT FOUND IN STREAMLIT SECRETS"

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "You are a poetry analysis expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
