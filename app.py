import streamlit as st
from core.foundation_model import foundation_reasoning
from core.prompt_engine import build_prompt

st.title("📊 Turkic Literature AI")

poem = st.text_area("Enter poem")

if st.button("Run Analysis"):

    result = foundation_reasoning(poem)

    st.subheader("Alignment")
    st.write(result["alignment"])

    st.subheader("Intertext")
    st.write(result["intertext"])

    prompt = build_prompt(
        poem,
        context=result,
        citations=result.get("citations", [])
    )

    st.subheader("Prompt")
    st.code(prompt)
