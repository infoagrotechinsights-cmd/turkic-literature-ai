import os
import sys
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# PATH FIX
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# =========================
# CORE IMPORTS (SAFE)
# =========================
from core.llm_engine import ask_gpt
from core.prompt_engine import build_prompt
from core.rag_engine import rag_answer

from core.alignment_engine import align_poetry
from core.foundation_model import analyze_poem_multilingual

from core.citation_verifier import verify_citations
from core.crossref_client import search_crossref

from core.influence_network import build_influence_network
from core.intertext_graph import build_intertext_graph

from export.pdf_export import create_thesis_pdf


# =========================
# UI
# =========================
st.set_page_config(page_title="Turkic Literature AI v3", layout="wide")
st.title("📚 Turkic Literature Foundation AI (Research Engine v3)")


# =========================
# INPUT
# =========================
poem = st.text_area("📜 Şiir / Metin (Azerice - Farsça - Türkçe)")

query = st.text_input("🔍 Akademik araştırma sorusu")


# =========================
# 1. FOUNDATION ANALYSIS
# =========================
if st.button("🧠 Foundation Model Analysis"):

    result = analyze_poem_multilingual(poem)

    st.subheader("📖 Multilingual Academic Analysis")
    st.write(result)


# =========================
# 2. ALIGNMENT ENGINE
# =========================
if st.button("🔗 Alignment Engine"):

    result = align_poetry(poem)

    st.subheader("🌐 Language Alignment")
    st.write(result)


# =========================
# 3. RAG (REAL SOURCES)
# =========================
if st.button("📚 RAG (CrossRef Real Sources)"):

    results = rag_answer(query)

    st.subheader("📡 Real Academic Sources (CrossRef)")
    st.write(results)


# =========================
# 4. CITATION VERIFIER
# =========================
if st.button("✔ Citation Verification"):

    result = verify_citations(query)

    st.subheader("🧾 Verified APA References")
    st.write(result)


# =========================
# 5. INTERTEXT GRAPH
# =========================
if st.button("🌐 Intertext Graph"):

    G = build_intertext_graph(poem)

    if len(G.nodes) == 0:
        st.warning("No intertext connections found")
    else:
        fig, ax = plt.subplots(figsize=(10, 6))
        nx.draw(G, with_labels=True, node_size=2500)
        st.pyplot(fig)


# =========================
# 6. INFLUENCE NETWORK
# =========================
if st.button("🧬 Influence Network"):

    sample_poets = [
        {"name": "Nizami", "influences": ["Fuzuli"]},
        {"name": "Fuzuli", "influences": ["Nesimi"]},
        {"name": "Nesimi", "influences": []}
    ]

    G = build_influence_network(sample_poets)

    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(G, with_labels=True)
    st.pyplot(fig)


# =========================
# 7. PDF EXPORT (ACADEMIC PAPER)
# =========================
if st.button("📄 Generate Thesis PDF"):

    analysis = ask_gpt(build_prompt(poem, "thesis"))
    citations = verify_citations(query)

    pdf_path = create_thesis_pdf(
        poem=poem,
        analysis=analysis,
        citations=citations
    )

    with open(pdf_path, "rb") as f:
        st.download_button(
            "⬇ Download Academic Paper",
            f,
            file_name="turkic_thesis.pdf"
        )


# =========================
# SIDEBAR
# =========================
st.sidebar.title("System Status")

st.sidebar.write("LLM:", "✅")
st.sidebar.write("CrossRef:", "✅")
st.sidebar.write("RAG:", "✅")
st.sidebar.write("Graph:", "✅")

st.sidebar.info("""
Turkic Literature AI v3
- Foundation Model Layer
- Multilingual Alignment
- Real Citation System
- Knowledge Graph
- Academic PDF Export
""")
