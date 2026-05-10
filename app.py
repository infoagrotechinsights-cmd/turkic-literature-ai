import sys
import os

# =========================
# 🔧 ROOT FIX (CRITICAL)
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
from core.intertext_graph import build_intertext_graph
from core.citation_system import format_citations
from core.rag_engine import rag_answer
from core.literature_review import generate_review
from core.influence_timeline import build_timeline

# =========================
# VIZ (SAFE IMPORT)
# =========================
import viz.graph as vg
build_graph = vg.build_graph

from export.pdf_export import create_thesis_pdf


# =========================
# UI
# =========================
st.title("📚 PoetryGPT – Turkic Literature AI")

poem = st.text_area("Enter poem")

if st.button("Graph"):
    data = build_timeline()
    G = build_graph(data)

    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True)
    st.pyplot(fig)
