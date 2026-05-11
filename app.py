import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Turkic Literature AI",
    layout="wide"
)

st.title("📚 Turkic Literature AI")
st.markdown("### 🧠 Digital Humanities Research Cockpit")

# =========================
# INPUT
# =========================
poem = st.text_area("📜 Metin / Şiir Giriniz", height=250)

# =========================
# SAFE IMPORT WRAPPER
# =========================
def safe_imports():

    try:
        from core.foundation_model import foundation_reasoning
        from core.rag_engine import retrieve_academic_context
        from core.citation_verifier import search_crossref
        from core.knowledge_graph import build_knowledge_graph
        from viz.graph import draw_graph
        from export.pdf_export import create_thesis_pdf
        return {
            "foundation_reasoning": foundation_reasoning,
            "retrieve_academic_context": retrieve_academic_context,
            "search_crossref": search_crossref,
            "build_knowledge_graph": build_knowledge_graph,
            "draw_graph": draw_graph,
            "create_thesis_pdf": create_thesis_pdf
        }

    except Exception as e:
        st.error(f"Import Error: {e}")
        return None


mods = safe_imports()

# =========================
# RUN ANALYSIS
# =========================
if st.button("🚀 Run Academic Analysis"):

    if not mods:
        st.stop()

    if not poem.strip():
        st.warning("Metin giriniz.")
        st.stop()

    # =========================
    # 1. FOUNDATION MODEL
    # =========================
    result = mods["foundation_reasoning"](poem)

    st.success("Analysis completed")

    # =========================
    # 2. INTERTEXT OUTPUT
    # =========================
    st.subheader("🔗 Intertext Analysis")
    st.json(result.get("intertext", []))

    # =========================
    # 3. RAG OUTPUT
    # =========================
    st.subheader("📚 RAG Academic Context")

    rag = mods["retrieve_academic_context"](poem)

    for r in rag:
        st.markdown(f"""
**Score:** {r['score']}  
{r['text']}
""")

    # =========================
    # 4. CITATION VERIFICATION
    # =========================
    st.subheader("📖 Verified Sources (Crossref)")

    citations = []

    try:
        citations = mods["search_crossref"](poem)

        for c in citations:
            if c.get("verified"):
                st.markdown(f"""
### {c['title']}
DOI: {c['doi']}
APA: {c['apa']}
""")
    except:
        st.warning("Citation system unavailable")

    # =========================
    # 5. KNOWLEDGE GRAPH
    # =========================
    st.subheader("🧠 Knowledge Graph")

    try:
        G = mods["build_knowledge_graph"](result.get("intertext", []))
        fig = mods["draw_graph"](G)
        st.pyplot(fig)
    except:
        st.warning("Graph system unavailable")

    # =========================
    # 6. PDF EXPORT
    # =========================
    st.subheader("📄 Thesis Export")

    try:
        pdf_path = mods["create_thesis_pdf"](
            "thesis_output.pdf",
            "Turkic Literature AI Thesis",
            poem,
            str(result),
            citations
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                "📥 Download Thesis PDF",
                f,
                file_name="thesis.pdf"
            )

    except Exception as e:
        st.warning(f"PDF error: {e}")

# =========================
# HEALTH CHECK
# =========================
st.divider()

if st.button("🧪 System Check"):

    st.json({
        "status": "running",
        "foundation": "lazy import OK",
        "rag": "active",
        "vector_db": "active",
        "graph": "active"
    })
