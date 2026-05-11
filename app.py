import os

# =========================
# 🔥 STABILITY FIXES
# =========================
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
os.environ["TRANSFORMERS_NO_TORCHVISION"] = "1"
os.environ["TRANSFORMERS_NO_TF"] = "1"

import streamlit as st

# =========================
# CORE IMPORTS (SAFE)
# =========================
try:
    from api.orchestrator import run_pipeline
except Exception as e:
    run_pipeline = None
    print("Orchestrator load error:", e)


# =========================
# UI CONFIG
# =========================
st.set_page_config(
    page_title="Turkic Literature AI",
    layout="wide"
)

st.title("📚 Turkic Literature AI")
st.subheader("Academic Research Cockpit (Semantic Engine)")

# =========================
# INPUT
# =========================
poem = st.text_area("📜 Paste poem or literary text", height=200)

run_btn = st.button("Analyze")

# =========================
# SAFE EXECUTION WRAPPER
# =========================
def safe_run(poem_text: str):

    if run_pipeline is None:
        return {
            "error": "Pipeline not loaded",
            "alignment": [],
            "intertext": [],
            "motifs": [],
            "citations": []
        }

    try:
        result = run_pipeline(poem_text)

        # 🔥 safety normalization (crash prevention)
        if not isinstance(result, dict):
            return {
                "error": "Invalid pipeline output",
                "raw": str(result)
            }

        result.setdefault("alignment", [])
        result.setdefault("intertext", [])
        result.setdefault("motifs", [])
        result.setdefault("citations", [])

        return result

    except Exception as e:
        return {
            "error": str(e),
            "alignment": [],
            "intertext": [],
            "motifs": [],
            "citations": []
        }


# =========================
# RENDER
# =========================
if run_btn and poem:

    result = safe_run(poem)

    st.markdown("## 📚 Academic Analysis (PhD Level)")

    # -------------------------
    # ERROR SAFE DISPLAY
    # -------------------------
    if "error" in result:
        st.error(result["error"])

    # -------------------------
    # MOTIFS / INTERTEXT
    # -------------------------
    st.markdown("### 📌 Metinlerarasılık Katmanı")

    motifs = result.get("motifs", [])

    if motifs and len(motifs) > 0:

        for m in motifs:
            term = m.get("term", "unknown")
            mtype = m.get("type", "unknown")
            score = m.get("score", 0.0)

            st.write(f"""
**{term}** → {mtype} (score: {round(float(score), 3)})
Metinlerarasılık açısından sembolik/kültürel katman üretir.
""")
    else:
        st.info("Motif bulunamadı.")

    # -------------------------
    # INTERTEXT
    # -------------------------
    st.markdown("### 🔗 Intertext Relations")

    intertext = result.get("intertext", [])

    if intertext:
        for i in intertext:
            st.write(f"- {i.get('term','?')} ({i.get('type','?')})")
    else:
        st.info("Intertext relation bulunamadı.")

    # -------------------------
    # ALIGNMENT SCORE
    # -------------------------
    st.markdown("### 🧠 Alignment Score")

    alignment = result.get("alignment", [])

    if alignment:
        for a in alignment:
            st.write(f"{a}")
    else:
        st.info("Alignment data yok.")

    # -------------------------
    # RAG CONTEXT
    # -------------------------
    st.markdown("### 📖 Academic Context (RAG)")

    rag = result.get("rag_context", None)
    if rag:
        st.write(rag)
    else:
        st.info("RAG context bulunamadı.")

    # -------------------------
    # CITATIONS
    # -------------------------
    st.markdown("### 📚 Verified Sources")

    citations = result.get("citations", [])

    if citations:
        for c in citations:
            st.write(c)
    else:
        st.info("No verified DOI sources detected.")

    # -------------------------
    # KNOWLEDGE GRAPH
    # -------------------------
    st.markdown("### 🧠 Knowledge Graph")

    kg = result.get("knowledge_graph", None)

    if kg:
        st.write(kg)
    else:
        st.info("Graph unavailable")

    # -------------------------
    # EXPORT
    # -------------------------
    st.markdown("### 📄 Thesis Export")
    st.code(str(result), language="json")
