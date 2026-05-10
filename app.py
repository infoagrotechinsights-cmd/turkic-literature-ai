import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# CORE IMPORTS
# =========================
from core.llm_engine import ask_gpt
from core.prompt_engine import build_prompt
from core.intertext_graph import build_intertext_graph
from core.citation_system import format_citations
from core.rag_engine import rag_answer
from core.literature_review import generate_review
from core.influence_timeline import build_timeline
from viz.graph import build_graph

from export.pdf_export import create_thesis_pdf


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="PoetryGPT - Turkic Literature AI",
    layout="wide"
)

st.title("📚 PoetryGPT – Turkic Literature AI")

st.markdown("""
AI-powered Digital Humanities system for:

- Turkic Literature
- Ottoman Poetry
- Persian Influence Mapping
- Intertextuality Analysis
- Academic RAG Engine
- Literary Knowledge Graph
""")


# =========================
# INPUT
# =========================
poem = st.text_area("✍️ Enter a poem", height=200)

mode = st.selectbox(
    "🎯 Analysis Mode",
    ["academic", "intertextuality", "thesis"]
)


# =========================
# ANALYSIS ENGINE
# =========================
if st.button("🚀 Analyze Poem"):

    if not poem:
        st.warning("Please enter a poem.")
        st.stop()

    prompt = build_prompt(poem, mode)

    result = ask_gpt(prompt)

    st.subheader("🧠 AI Analysis")
    st.write(result)

    st.subheader("📚 Citations")
    st.text(format_citations("Anonymous"))


# =========================
# INTERTEXT GRAPH
# =========================
if st.button("🌐 Show Intertext Graph"):

    if not poem:
        st.warning("Please enter a poem.")
        st.stop()

    G = build_intertext_graph(poem)

    if len(G.nodes) == 0:
        st.warning("No intertextual links found.")
    else:
        fig, ax = plt.subplots(figsize=(10, 6))

        pos = nx.spring_layout(G, seed=42)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=3000,
            font_size=10
        )

        st.pyplot(fig)


# =========================
# THESIS PDF EXPORT
# =========================
if st.button("📄 Generate Thesis PDF"):

    if not poem:
        st.warning("Please enter a poem.")
        st.stop()

    analysis = ask_gpt(build_prompt(poem, "thesis"))
    citations = format_citations("Anonymous")

    pdf_file = create_thesis_pdf(
        poem=poem,
        analysis=analysis,
        citations=citations
    )

    st.success("Thesis PDF generated!")

    with open(pdf_file, "rb") as f:
        st.download_button(
            "⬇ Download PDF",
            f,
            file_name="poetry_thesis.pdf"
        )


# =========================
# RAG SYSTEM
# =========================
st.divider()

st.header("📚 Academic RAG System")

query = st.text_input("Ask about Turkic poetry")


# -------------------------
# RAG SEARCH
# -------------------------
if st.button("🔎 RAG Search"):

    if not query:
        st.warning("Enter a question.")
        st.stop()

    result = rag_answer(query)

    st.subheader("📖 Academic Answer")
    st.write(result)


# -------------------------
# LITERATURE REVIEW
# -------------------------
if st.button("📚 Literature Review"):

    if not query:
        st.warning("Enter a topic.")
        st.stop()

    review = generate_review(query)

    st.subheader("🧠 Literature Review")
    st.write(review)


# -------------------------
# INFLUENCE TIMELINE
# -------------------------
if st.button("📈 Influence Timeline"):

    data = build_timeline()

    G = build_graph(data)

    fig, ax = plt.subplots(figsize=(12, 7))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3500,
        font_size=10
    )

    st.pyplot(fig)


# =========================
# SIDEBAR
# =========================
st.sidebar.title("ℹ️ About")

st.sidebar.info(
"""
PoetryGPT – Digital Humanities AI System

Features:
✔ Academic Analysis
✔ Intertext Graph
✔ Thesis PDF Export
✔ RAG Engine (safe mode)
✔ Literature Review Generator
✔ Influence Timeline
"""
)
