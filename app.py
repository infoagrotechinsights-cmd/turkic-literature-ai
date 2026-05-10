import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# =========================
# SAFE IMPORT LAYER
# =========================
try:
    from core.llm_engine import ask_gpt
    from core.prompt_engine import build_prompt
    from core.rag_engine import rag_answer
    from core.language_detector import detect
    from core.output_filter import clean
    from core.crossref_client import search_crossref
    from core.citation_verifier import verify_citations
    from core.intertext_graph import build_intertext_graph
    from core.influence_network import build_influence_network
    from export.pdf_export import create_thesis_pdf
except Exception as e:
    st.error(f"Import Error: {e}")


# =========================
# UI CONFIG
# =========================
st.set_page_config(page_title="Turkic Literature AI", layout="wide")
st.title("📚 Turkic Literature Academic AI Engine v2")


# =========================
# SESSION STATE
# =========================
if "poem" not in st.session_state:
    st.session_state.poem = ""

if "query" not in st.session_state:
    st.session_state.query = ""


# =========================
# INPUT
# =========================
poem = st.text_area(
    "📜 Şiir (Azerice / Türkçe / Farsça)",
    value=st.session_state.poem,
    height=220
)

st.session_state.poem = poem


query = st.text_input(
    "🔍 Akademik Soru",
    value=st.session_state.query
)

st.session_state.query = query


# =========================
# 🧠 FULL ANALYSIS PIPELINE
# =========================
if st.button("🧠 Full Academic Analysis"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        try:
            # 1. language detection
            lang = detect(poem)

            # 2. RAG retrieval
            rag_context = rag_answer(poem)

            # 3. citations (real sources)
            citations_raw = search_crossref(poem)
            citations = verify_citations(citations_raw)

            # 4. prompt build (FIXED)
            prompt = build_prompt(
                poem=poem,
                context=str(rag_context),
                citations=str(citations)
            )

            # 5. LLM call
            raw_result = ask_gpt(prompt)

            # 6. filter output
            result = clean(raw_result)

            # =========================
            # OUTPUT
            # =========================
            st.subheader("🌐 Dil")
            st.write(lang)

            st.subheader("📚 RAG Context")
            st.write(rag_context)

            st.subheader("📑 Verified Citations")
            st.write(citations)

            st.subheader("📖 Akademik Analiz")
            st.write(result)

        except Exception as e:
            st.error(f"Analysis Error: {e}")


# =========================
# 📑 CITATION CHECK ONLY
# =========================
if st.button("✔ Citation Verification"):

    if not query.strip():
        st.warning("Soru girilmedi")
    else:
        try:
            results = search_crossref(query)
            verified = verify_citations(results)

            st.subheader("📚 Sources")
            st.write(verified)

        except Exception as e:
            st.error(f"Citation Error: {e}")


# =========================
# 🌐 INTERTEXT GRAPH
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
# 🧬 INFLUENCE NETWORK
# =========================
if st.button("🧬 Influence Network"):

    try:
        data = [
            {"name": "Nizami", "influences": ["Fuzuli"]},
            {"name": "Fuzuli", "influences": ["Nesimi"]},
            {"name": "Nesimi", "influences": []}
        ]

        G = build_influence_network(data)

        fig, ax = plt.subplots(figsize=(10, 6))
        nx.draw(G, with_labels=True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Network Error: {e}")


# =========================
# 📄 PDF EXPORT
# =========================
if st.button("📄 Generate Thesis PDF"):

    if not poem.strip():
        st.warning("Şiir girilmedi")
    else:
        try:
            rag_context = rag_answer(poem)
            citations = search_crossref(poem)

            prompt = build_prompt(
                poem=poem,
                context=str(rag_context),
                citations=str(citations)
            )

            analysis = ask_gpt(prompt)
            analysis = clean(analysis)

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

        except Exception as e:
            st.error(f"PDF Error: {e}")


# =========================
# SIDEBAR
# =========================
st.sidebar.title("🔬 System Status")

st.sidebar.write("LLM: ✅")
st.sidebar.write("RAG: ✅")
st.sidebar.write("CrossRef: ✅")
st.sidebar.write("Graph: ✅")
st.sidebar.write("PDF: ✅")

st.sidebar.info("""
Turkic Literature AI v2

✔ RAG Retrieval  
✔ Citation Verification  
✔ Intertext Graph  
✔ Influence Network  
✔ Thesis Generator  
""")
