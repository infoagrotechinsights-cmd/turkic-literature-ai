import streamlit as st
from core.analysis_engine import analyze_poem

st.title("PoetryGPT")

poem = st.text_area("Enter poem")

analysis_type = st.selectbox(
    "Analysis Type",
    [
        "Academic",
        "Intertextuality",
        "Symbolic"
    ]
)

if st.button("Analyze"):

    result = analyze_poem(
        poem,
        analysis_type
    )

    st.write(result)
