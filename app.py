import os
import sys
import streamlit as st

# =========================
# 🔧 PATH FIX (CRITICAL)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, "..")))

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
# SAFE VIZ IMPORT
# =========================
try:
    import viz.graph as vg
    build_graph = vg.build_graph
except Exception:
    build_graph = None


# =========================
# UI
# =========================
st.set_page_config(page_title="PoetryGPT", layout="wide")
st.title("📚 PoetryGPT – Turkic Literature AI")


# =========================
# INPUT
# =========================
mode = st.radio("Input Mode", ["✍️ Paste Text", "📄 Upload File"])

poem = ""

if mode == "✍️ Paste Text":
    poem = st.text_area("Enter poem", height=250)

elif mode == "📄 Upload File":
    file = st.file_uploader("Upload TXT", type=["txt"])
    if file:
        poem = file.read().decode("utf-8")
        st.text_area("Loaded", poem, height=250)


analysis_mode = st.selectbox("Analysis Type", ["academic", "intertextuality", "thesis"])


# =========================
# ANALYSIS
# =========================
if st.button("🚀 Analyze"):

    if not poem.strip():
        st.warning("No input")
        st.stop()

    prompt = build_prompt(poem, analysis_mode)
    result = ask_gpt(prompt)

    st.subheader("🧠 AI Analysis")
    st.write(result)

    st.subheader("📚 Citations")
    st.text(format_citations())


# =========================
# GRAPH
# =========================
if st.button("🌐 Graph"):

    G = build_intertext_graph(poem)

    if len(G.nodes) == 0:
        st.warning("No relations found")
    else:
        fig, ax = plt.subplots()
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_size=2500)
        st.pyplot(fig)


# =========================
# PDF EXPORT
# =========================
if st.button("📄 Thesis PDF"):

    analysis = ask_gpt(build_prompt(poem, "thesis"))

    pdf = create_thesis_pdf(
        poem=poem,
        analysis=analysis,
        citations=format_citations()
    )

    with open(pdf, "rb") as f:
        st.download_button("Download PDF", f, file_name="thesis.pdf")


# =========================
# RAG
# =========================
st.divider()
st.header("📚 RAG SYSTEM")

query = st.text_input("Ask question")

if st.button("Search RAG"):
    st.write(rag_answer(query))

if st.button("Literature Review"):
    st.write(generate_review(query))

if st.button("Timeline"):
    data = build_timeline()

    if build_graph:
        G = build_graph(data)
        fig, ax = plt.subplots()
        nx.draw(G, with_labels=True)
        st.pyplot(fig)
    else:
        st.warning("Graph module missing")


# =========================
# SIDEBAR
# =========================
st.sidebar.title("PoetryGPT")
st.sidebar.info("AI Poetry + RAG + Graph + Thesis System")
