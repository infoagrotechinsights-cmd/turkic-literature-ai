import streamlit as st

st.set_page_config(
    page_title="Turkic Literature AI",
    layout="wide"
)

st.title("📚 Academic Research Cockpit")
st.markdown("🧠 Digital Humanities AI System")

# =========================
# INPUT
# =========================
poem = st.text_area("📜 Paste poem or literary text", height=250)

# =========================
# SAFE IMPORTS
# =========================
def load_modules():
    try:
        from api.orchestrator import Orchestrator
        from core.academic_renderer import render_academic_output
        return Orchestrator(), render_academic_output
    except Exception as e:
        st.error(f"System Load Error: {e}")
        return None, None


orch, render_academic_output = load_modules()

# =========================
# RUN BUTTON
# =========================
if st.button("🚀 Run Academic Analysis"):

    if not orch:
        st.stop()

    if not poem.strip():
        st.warning("Please enter a text.")
        st.stop()

    # =========================
    # PIPELINE RUN
    # =========================
    result = orch.run(poem)

    st.success("Analysis completed")

    # =========================
    # 🧠 ACADEMIC OUTPUT (MAIN)
    # =========================
    try:
        academic_text = render_academic_output(poem, result)

        st.subheader("📚 Academic Analysis (PhD Level)")
        st.markdown(academic_text)

    except Exception as e:
        st.error(f"Rendering error: {e}")

    # =========================
    # 📚 RAG CONTEXT
    # =========================
    st.subheader("📖 Academic Context (RAG)")

    try:
        for r in result.get("rag", []):
            st.markdown(f"**{r['score']}** → {r['text']}")
    except:
        st.warning("RAG unavailable")

    # =========================
    # 📖 CITATIONS
    # =========================
    st.subheader("📖 Verified Sources")

    try:
        for c in result.get("citations", []):
            if c.get("verified"):
                st.markdown(f"""
**{c.get('title','Unknown')}**  
DOI: {c.get('doi','N/A')}  
{c.get('apa','')}
""")
    except:
        st.warning("Citation system unavailable")

    # =========================
    # 🧠 GRAPH
    # =========================
    st.subheader("🧠 Knowledge Graph")

    try:
        from core.knowledge_graph import build_knowledge_graph
        from viz.graph import draw_graph

        G = build_knowledge_graph(result.get("intertext", []))
        fig = draw_graph(G)
        st.pyplot(fig)

    except:
        st.warning("Graph unavailable")

    # =========================
    # 📄 PDF EXPORT
    # =========================
    st.subheader("📄 Thesis Export")

    try:
        from export.pdf_export import create_thesis_pdf

        pdf_path = create_thesis_pdf(
            "thesis_output.pdf",
            "Turkic Literature AI Thesis",
            poem,
            str(result.get("intertext", [])),
            result.get("citations", [])
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
# SYSTEM CHECK
# =========================
st.divider()

if st.button("🧪 System Check"):

    st.json({
        "status": "OK",
        "mode": "Academic Research Cockpit",
        "layers": [
            "Orchestrator",
            "RAG",
            "Vector DB",
            "Citation Verifier",
            "Knowledge Graph",
            "PDF Export"
        ]
    })
