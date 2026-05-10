import streamlit as st

from core.prompt_engine import build_prompt
from core.llm_engine import ask_gpt
from core.citation_system import generate_citation
from core.intertext import detect_intertext
from export.pdf_export import create_pdf

st.title("PoetryGPT – Turkic Literature AI")

poem = st.text_area("Poem")

mode = st.selectbox(
    "Mode",
    ["academic", "intertextuality", "thesis"]
)

if st.button("Analyze"):

    prompt = build_prompt(poem, mode)
    result = ask_gpt(prompt)

    st.subheader("AI Analysis")
    st.write(result)

    st.subheader("Intertextuality")
    st.write(detect_intertext(poem))

    st.subheader("Citation")
    st.write(generate_citation("Anonymous"))

    if mode == "thesis":
        pdf = create_pdf(result)
        st.success("PDF generated")
