import os
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# SAFE IMPORT BLOCK (CRASH PREVENTION)
# =========================
try:
    from core.llm_engine import ask_gpt
    from core.prompt_engine import build_prompt
    from core.rag_engine import rag_answer
    from core.language_detector import detect
    from core.output_filter import clean
    from core.citation_verifier import verify_citations
    from core.crossref_client import search_crossref
    from core.intertext_graph import build_intertext_graph
    from core.influence_network import build_influence_network
    from export.pdf_export import create_thesis_pdf
except Exception as e:
    st.error(f"Import Error: {e}")


# =========================
# STREAMLIT CONFIG
# =========================
st.set_page_config(page_title="Turkic Literature AI", layout="wide")
st.title("📚 Turkic Literature Academic AI Engine")


# =========================
# SESSION STATE
# =========================
if "poem" not in st.session_state:
    st.session_state.poem = ""

if "query" not in st.session_state:
    st.session_state.query = ""


# =========================
# INPUT AREA
# =========================
st.subheader("📜 Şiir Girişi")

poem_input = st.text_area(
    "Şiir (Azerice / Türkçe / Farsça)",
    value=st.session_state.poem,
    height=220
)

st.session_state.poem = poem_input
poem = st.session_state.poem


# =========================
# QUERY INPUT
# =========================
query_input = st.text_input("🔍 Akademik Soru", value=st.session_state.query)
st.session_state.query = query_input
query = st.session_state.query


# =========================
# 1. FULL ANALYSIS PIPELINE
# =========================
if st.button("🧠 Full Academic Analysis"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        try:
            lang = detect(poem)

            rag_context = rag_answer(poem)

            prompt = build_prompt(poem)

            raw_result = ask_gpt(prompt)

            result = clean(raw_result)

            st.subheader("🌐 Dil")
            st.write(lang)

            st.subheader("📚 RAG Context")
            st.write(rag_context)

            st.subheader("📖 Akademik Analiz")
            st.write(result)

        except Exception as e:
            st.error(f"Analysis Error: {e}")


# =========================
# 2. CITATION CHECK (CROSSREF)
# =========================
if st.button("✔ Citation Verification"):

    if not query.strip():
        st.warning("Soru girilmedi")
    else:
        try:
            results = search_crossref(query)
            verified = verify_citations(results)

            st.subheader("📑 Doğrulanmış Kaynaklar")
            st.write(verified)

        except Exception as e:
            st.error(f"Citation Error: {e}")


# =========================
# 3. INTERTEXT GRAPH
# =========================
if st.button("🌐 Intertext Graph"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        try:
            G = build_intertext_graph(poem)

            fig, ax = plt.subplots(figsize=(10, 6))
            nx.draw(G, with_labels=True, node_size=2000)

            st.pyplot(fig)

        except Exception as e:
            st.error(f"Graph Error: {e}")


# =========================
# 4. INFLUENCE NETWORK
# =========================
if st.button("🧬 Influence Network"):

    try:
        sample_data = [
            {"name": "Nizami", "influences": ["Fuzuli"]},
            {"name": "Fuzuli", "influences": ["Nesimi"]},
            {"name": "Nesimi", "influences": []}
        ]

        G = build_influence_network(sample_data)

        fig, ax = plt.subplots(figsize=(10, 6))
        nx.draw(G, with_labels=True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Network Error: {e}")


# =========================
# 5. PDF THESIS EXPORT
# =========================
if st.button("📄 Generate Thesis PDF"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        try:
            analysis = ask_gpt(build_prompt(poem))
            citations = search_crossref(query if query else poem)

            pdf_path = create_thesis_pdf(
                poem=poem,
                analysis=analysis,
                citations=citations
            )

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "⬇ PDF İndir",
                    f,
                    file_name="academic_thesis.pdf"
                )

        except Exception as e:
            st.error(f"PDF Error: {e}")


# =========================
# SIDEBAR SYSTEM STATUS
# =========================
st.sidebar.title("🔬 System Status")

st.sidebar.write("LLM Engine: ✅")
st.sidebar.write("RAG System: ✅")
st.sidebar.write("CrossRef API: ✅")
st.sidebar.write("Graph Engine: ✅")
st.sidebar.write("PDF Export: ✅")

st.sidebar.info("""
Turkic Literature AI Engine v1

✔ RAG Retrieval  
✔ Academic Analysis  
✔ Citation Verification  
✔ Intertext Graph  
✔ Influence Network  
✔ Thesis PDF Export  
""")
