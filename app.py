import os
import sys

# =========================
# 🔧 CRITICAL PATH FIX
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# CORE MODULES
# =========================
from core.llm_engine import ask_gpt
from core.prompt_engine import build_prompt
from core.rag_engine import rag_answer
from core.literature_review import generate_review
from core.influence_timeline import build_timeline
from core.citation_system import format_citations
from core.intertext_graph import build_intertext_graph

# =========================
# SAFE VIZ IMPORT
# =========================
import viz.graph as vg
build_graph = vg.build_graph

from export.pdf_export import create_thesis_pdf


# =========================
# UI
# =========================
st.set_page_config(
    page_title="PoetryGPT - Turkic Literature AI",
    layout="wide"
)

st.title("📚 PoetryGPT – AI Poetry Analysis System")


# =========================
# INPUT MODE
# =========================
mode = st.radio(
    "Input Mode",
    ["✍️ Paste Text", "📄 Upload File"]
)

poem = ""


# =========================
# TEXT INPUT
# =========================
if mode == "✍️ Paste Text":
    poem = st.text_area("Enter poem", height=250)


# =========================
# FILE UPLOAD
# =========================
elif mode == "📄 Upload File":
    file = st.file_uploader("Upload poem (.txt)", type=["txt"])

    if file is not None:
        poem = file.read().decode("utf-8")
        st.text_area("Loaded Poem", poem, height=250)


# =========================
# ANALYSIS MODE
# =========================
analysis_mode = st.selectbox(
    "Analysis Type",
    ["academic", "intertextuality", "thesis"]
)


# =========================
# MAIN ANALYSIS
# =========================
if st.button("🚀 Analyze Poem"):

    if not poem.strip():
        st.warning("Please input or upload a poem.")
        st.stop()

    st.subheader("📖 Input Poem")
    st.write(poem)

    prompt = build_prompt(poem, analysis_mode)
    result = ask_gpt(prompt)

    st.subheader("🧠 AI Analysis")
    st.write(result)

    st.subheader("📚 Citations")
    st.text(format_citations("Anonymous"))


# =========================
# INTERTEXT GRAPH
# =========================
if st.button("🌐 Intertext Graph"):

    G = build_intertext_graph(poem)

    if len(G.nodes) == 0:
        st.warning("No intertextual connections found.")
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

    if not poem.strip():
        st.warning("No poem provided.")
        st.stop()

    analysis = ask_gpt(build_prompt(poem, "thesis"))

    pdf_file = create_thesis_pdf(
        poem=poem,
        analysis=analysis,
        citations=format_citations("Anonymous")
    )

    with open(pdf_file, "rb") as f:
        st.download_button(
            "⬇ Download Thesis PDF",
            f,
            file_name="poetry_thesis.pdf"
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
st.sidebar.title("ℹ️ PoetryGPT AI System")

st.sidebar.info(
"""
✔ Paste / Upload Input  
✔ AI Poem Analysis  
✔ Intertext Graph  
✔ RAG Engine  
✔ Literature Review  
✔ Thesis PDF Export  
"""
)
