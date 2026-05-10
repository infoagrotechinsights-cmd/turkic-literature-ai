import os
import sys

# =========================
# 🔧 PATH FIX (CRITICAL)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# bazı Streamlit deploylarında gerekli fallback
sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, "..")))

import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# CORE IMPORTS
# =========================
from core.llm_engine import ask_gpt
from core.prompt_engine import build_prompt
from core.rag_engine import rag_answer
from core.literature_review import generate_review
from core.influence_timeline import build_timeline
from core.citation_system import format_citations
from core.intertext_graph import build_intertext_graph

from export.pdf_export import create_thesis_pdf

# =========================
# SAFE VIZ IMPORT (NO CRASH)
# =========================
try:
    import viz.graph as vg
    build_graph = vg.build_graph
except Exception:
    build_graph = None


# =========================
# UI
# =========================
st.set_page_config(
    page_title="PoetryGPT AI",
    layout="wide"
)

st.title("📚 PoetryGPT – Turkic Literature AI")


# =========================
# INPUT MODE
# =========================
mode = st.radio("Input Mode", ["✍️ Paste Text", "📄 Upload File"])

poem = ""

if mode == "✍️ Paste Text":
    poem = st.text_area("Enter poem", height=250)

elif mode == "📄 Upload File":
    file = st.file_uploader("Upload TXT file", type=["txt"])

    if file:
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
# ANALYZE
# =========================
if st.button("🚀 Analyze Poem"):

    if not poem.strip():
        st.warning("Please provide a poem.")
        st.stop()

    st.subheader("📖 Input")
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

        nx.draw(G, pos, with_labels=True, node_size=2500)
        st.pyplot(fig)


# =========================
# THESIS PDF
# =========================
if st.button("📄 Generate Thesis PDF"):

    if not poem.strip():
        st.warning("No poem provided")
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
st.header("📚 Academic RAG")

query = st.text_input("Ask about Turkic poetry")

if st.button("🔎 RAG Search"):
    st.write(rag_answer(query))

if st.button("📚 Literature Review"):
    st.write(generate_review(query))

if st.button("📈 Influence Timeline"):

    data = build_timeline()

    if build_graph:
        G = build_graph(data)
    else:
        st.warning("Graph module not available")
        st.stop()

    fig, ax = plt.subplots(figsize=(12, 7))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=2500)
    st.pyplot(fig)


# =========================
# SIDEBAR
# =========================
st.sidebar.title("PoetryGPT System")

st.sidebar.info(
"""
✔ Paste / Upload poems  
✔ AI analysis engine  
✔ RAG system  
✔ Intertext graph  
✔ Thesis PDF generator  
"""
)
