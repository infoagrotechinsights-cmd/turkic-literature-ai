import os

# =========================
# 🔥 SYSTEM STABILITY FLAGS
# =========================
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
os.environ["TRANSFORMERS_NO_TORCHVISION"] = "1"
os.environ["TRANSFORMERS_NO_TF"] = "1"

import streamlit as st

# =========================
# SAFE PIPELINE IMPORT
# =========================
run_pipeline = None
pipeline_error = None

try:
    from api.orchestrator import run_pipeline
except Exception as e:
    pipeline_error = str(e)

# =========================
# UI CONFIG
# =========================
st.set_page_config(
    page_title="Turkic Literature AI",
    layout="wide"
)

st.title("📚 Turkic Literature AI")
st.subheader("Semantic Academic Research Cockpit")

# =========================
# PIPELINE ERROR DISPLAY
# =========================
if pipeline_error:
    st.error("❌ Pipeline Load Error")
    st.code(pipeline_error)

# =========================
# INPUT
# =========================
poem = st.text_area("📜 Paste poem or literary text", height=220)

# =========================
# SAFE RUN FUNCTION
# =========================
def safe_run(text: str):

    if run_pipeline is None:
        return {
            "error": "Pipeline not loaded",
            "alignment": [],
            "intertext": [],
            "motifs": [],
            "rag_context": {},
            "citations": []
        }

    try:
        result = run_pipeline(text)

        if not isinstance(result, dict):
            return {
                "error": "Invalid pipeline output",
                "raw": str(result)
            }

        # SAFE DEFAULTS
        result.setdefault("alignment", [])
        result.setdefault("intertext", [])
        result.setdefault("motifs", [])
        result.setdefault("rag_context", {})
        result.setdefault("citations", [])
        result.setdefault("knowledge_graph", None)

        return result

    except Exception as e:
        return {
            "error": str(e),
            "alignment": [],
            "intertext": [],
            "motifs": [],
            "rag_context": {},
            "citations": []
        }

# =========================
# RUN BUTTON
# =========================
if st.button("Analyze") and poem:

    result = safe_run(poem)

    st.markdown("## 📚 Academic Analysis (PhD Level)")

    # =========================
    # ERROR BLOCK
    # =========================
    if result.get("error"):
        st.warning("⚠️ Analysis Error")
        st.code(result["error"])

    # =========================
    # MOTIFS
    # =========================
    st.markdown("### 📌 Metinlerarasılık Katmanı")

    motifs = result.get("motifs", [])

    if motifs:
        for m in motifs:
            st.write(
                f"**{m.get('term','?')}** → {m.get('type','?')} "
                f"(score: {m.get('score', 0)})"
            )
    else:
        st.info("Motif bulunamadı")

    # =========================
    # INTERTEXT
    # =========================
    st.markdown("### 🔗 Intertext Relations")

    intertext = result.get("intertext", [])

    if intertext:
        for i in intertext:
            st.write(i)
    else:
        st.info("Intertext relation bulunamadı")

    # =========================
    # ALIGNMENT
    # =========================
    st.markdown("### 🧠 Alignment Score")

    alignment = result.get("alignment", [])

    if alignment:
        st.json(alignment)
    else:
        st.info("Alignment data yok")

    # =========================
    # RAG
    # =========================
    st.markdown("### 📖 Academic Context (RAG)")

    st.json(result.get("rag_context", {}))

    # =========================
    # CITATIONS
    # =========================
    st.markdown("### 📚 Verified Sources")

    citations = result.get("citations", [])

    if citations:
        st.json(citations)
    else:
        st.info("No verified DOI sources detected")

    # =========================
    # KNOWLEDGE GRAPH
    # =========================
    st.markdown("### 🧠 Knowledge Graph")

    kg = result.get("knowledge_graph")

    if kg:
        st.json(kg)
    else:
        st.info("Graph unavailable")

    # =========================
    # RAW EXPORT
    # =========================
    st.markdown("### 📄 Thesis Export (Raw JSON)")
    st.code(result, language="json")
