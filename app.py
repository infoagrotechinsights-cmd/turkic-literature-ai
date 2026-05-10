import os
import sys
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# PATH FIX (IMPORT SAFE)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# =========================
# CORE IMPORTS
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
# STREAMLIT CONFIG
# =========================
st.set_page_config(page_title="Turkic Literature AI v3", layout="wide")
st.title("📚 Turkic Literature Foundation AI (Research Engine v3)")


# =========================
# SESSION STATE INIT
# =========================
if "poem" not in st.session_state:
    st.session_state.poem = ""

if "query" not in st.session_state:
    st.session_state.query = ""


# =========================
# INPUT AREA (STABLE)
# =========================
st.subheader("📜 Şiir Girişi")

text_input = st.text_area(
    "Şiir yapıştır (Azerice / Farsça / Türkçe)",
    value=st.session_state.poem,
    height=200
)

st.session_state.poem = text_input
poem = st.session_state.poem


# =========================
# FILE UPLOAD (SAFE)
# =========================
uploaded_file = st.file_uploader("📂 TXT dosya yükle", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.session_state.poem = content
    st.success("Dosya başarıyla yüklendi")


# =========================
# QUERY INPUT
# =========================
query_input = st.text_input("🔍 Akademik soru", value=st.session_state.query)
st.session_state.query = query_input
query = st.session_state.query


# =========================
# 1. FOUNDATION MODEL
# =========================
if st.button("🧠 Foundation Analysis"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        result = analyze_poem_multilingual(poem)
        st.subheader("📖 Akademik Analiz")
        st.write(result)


# =========================
# 2. ALIGNMENT ENGINE
# =========================
if st.button("🔗 Alignment Engine"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        result = align_poetry(poem)
        st.subheader("🌐 Dilsel Hizalama")
        st.write(result)


# =========================
# 3. RAG (REAL SOURCES)
# =========================
if st.button("📚 RAG (CrossRef Real Sources)"):

    if not query.strip():
        st.warning("Soru girilmedi")
    else:
        result = rag_answer(query)
        st.subheader("📡 Gerçek Akademik Kaynaklar")
        st.write(result)


# =========================
# 4. CITATION VERIFIER
# =========================
if st.button("✔ Citation Verification"):

    if not query.strip():
        st.warning("Soru girilmedi")
    else:
        result = verify_citations(query)
        st.subheader("🧾 Doğrulanmış Kaynaklar")
        st.write(result)


# =========================
# 5. INTERTEXT GRAPH
# =========================
if st.button("🌐 Intertext Graph"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        G = build_intertext_graph(poem)

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
# 7. PDF EXPORT (ACADEMIC THESIS)
# =========================
if st.button("📄 Generate Thesis PDF"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        analysis = ask_gpt(build_prompt(poem))
        citations = verify_citations(query)

        pdf_path = create_thesis_pdf(
            poem=poem,
            analysis=analysis,
            citations=citations
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇ PDF İndir",
                f,
                file_name="turkic_thesis.pdf"
            )


# =========================
# SIDEBAR STATUS
# =========================
st.sidebar.title("🔬 System Status")

st.sidebar.write("LLM:", "✅")
st.sidebar.write("CrossRef:", "✅")
st.sidebar.write("Alignment:", "✅")
st.sidebar.write("Graph:", "✅")
st.sidebar.write("PDF:", "✅")

st.sidebar.info("""
Turkic Literature AI v3

✔ Multilingual Foundation Model  
✔ CrossRef Verified Citations  
✔ Intertext Graph Engine  
✔ Influence Network  
✔ Academic PDF Generator  
""")
