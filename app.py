import sys
import os

# =========================
# 🔧 FIX: PATH RESOLVER (CRITICAL)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

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

# =========================
# SAFE VIZ IMPORT (NO CRASH)
# =========================
from viz.graph import build_graph

from export.pdf_export import create_thesis_pdf


# =========================
# UI
# =========================
st.set_page_config(
    page_title="PoetryGPT - Turkic Literature AI",
    layout="wide"
)

st.title("📚 PoetryGPT – Turkic Literature AI")

poem = st.text_area("✍️ Enter a poem", height=200)

mode = st.selectbox(
    "Analysis Mode",
    ["academic", "intertextuality", "thesis"]
)


# =========================
# ANALYSIS
# =========================
if st.button("🚀 Analyze Poem"):

    if not poem:
        st.warning("Enter a poem.")
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

    G = build_intertext_graph(poem)

    if len(G.nodes) == 0:
        st.warning("No links found.")
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
# THESIS PDF
# =========================
if st.button("📄 Generate Thesis PDF"):

    analysis = ask_gpt(build_prompt(poem, "thesis"))

    pdf_file = create_thesis_pdf(
        poem=poem,
        analysis=analysis,
        citations=format_citations("Anonymous")
    )

    with open(pdf_file, "rb") as f:
        st.download_button(
            "⬇ Download PDF",
            f,
            file_name="thesis.pdf"
        )


# =========================
# RAG SYSTEM
# =========================
st.divider()
st.header("📚 Academic RAG System")

query = st.text_input("Ask about Turkic poetry")


if st.button("🔎 RAG Search"):
    st.write(rag_answer(query))


if st.button("📚 Literature Review"):
    st.write(generate_review(query))


if st.button("📈 Influence Timeline"):

    data = build_timeline()
    G = build_graph(data)

    fig, ax = plt.subplots(figsize=(12, 7))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=3000)

    st.pyplot(fig)


# =========================
# SIDEBAR
# =========================
st.sidebar.info(
"""
PoetryGPT AI System:

✔ RAG Engine  
✔ Intertext Graph  
✔ Thesis Generator  
✔ Literature Review  
✔ Influence Timeline  
"""
)
