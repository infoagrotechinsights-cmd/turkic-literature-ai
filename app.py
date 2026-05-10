import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from core.llm_engine import ask_gpt
from core.prompt_engine import build_prompt
from core.intertext_graph import build_intertext_graph
from core.citation_system import format_citations
from export.pdf_export import create_thesis_pdf


# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="PoetryGPT - Turkic Literature AI",
    layout="wide"
)

st.title("📚 PoetryGPT – Turkic Literature AI")


# ---------------------------
# INPUT
# ---------------------------
poem = st.text_area("✍️ Şiiri giriniz", height=200)

mode = st.selectbox(
    "🎯 Analiz Modu",
    ["academic", "intertextuality", "thesis"]
)


# ---------------------------
# ANALYZE BUTTON
# ---------------------------
if st.button("🚀 Analyze Poem"):

    if not poem:
        st.warning("Lütfen bir şiir giriniz.")
        st.stop()

    # Prompt oluştur
    prompt = build_prompt(poem, mode)

    # LLM çağrısı
    result = ask_gpt(prompt)

    # -----------------------
    # OUTPUT: ANALYSIS
    # -----------------------
    st.subheader("🧠 AI Analysis")
    st.write(result)

    # -----------------------
    # CITATION
    # -----------------------
    citations = format_citations("Anonymous")

    st.subheader("📚 Citations")
    st.text(citations)

    # -----------------------
    # INTERTEXT SUMMARY
    # -----------------------
    st.subheader("🔗 Intertextuality Insights")

    st.info("Motif detection + cultural mapping active (MVP mode)")


# ---------------------------
# INTERTEXT GRAPH
# ---------------------------
if st.button("🌐 Show Intertext Graph"):

    G = build_intertext_graph(poem)

    if len(G.nodes) == 0:
        st.warning("No intertextual links detected.")
    else:
        fig, ax = plt.subplots()

        pos = nx.spring_layout(G, seed=42)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=2500,
            font_size=9
        )

        st.pyplot(fig)


# ---------------------------
# THESIS PDF EXPORT
# ---------------------------
if st.button("📄 Generate Thesis PDF"):

    if not poem:
        st.warning("Önce şiir giriniz.")
        st.stop()

    prompt = build_prompt(poem, "thesis")
    analysis = ask_gpt(prompt)
    citations = format_citations("Anonymous")

    pdf_file = create_thesis_pdf(
        poem=poem,
        analysis=analysis,
        citations=citations
    )

    st.success("Thesis PDF generated successfully!")

    with open(pdf_file, "rb") as f:
        st.download_button(
            "⬇ Download Thesis PDF",
            f,
            file_name="poetry_thesis.pdf"
        )


# ---------------------------
# SIDEBAR INFO
# ---------------------------
st.sidebar.title("ℹ️ About")

st.sidebar.info(
"""
PoetryGPT is an AI-powered literary research system for:
- Turkic literature
- Azerbaijani poetry
- Ottoman poetry
- Persian influence mapping

Features:
✔ Academic analysis  
✔ Intertextuality graph  
✔ Thesis PDF generator  
✔ Citation engine  
"""
)
