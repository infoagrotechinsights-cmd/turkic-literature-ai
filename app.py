import streamlit as st

# =========================
# CORE IMPORTS (SAFE LAYER)
# =========================

from core.foundation_model import foundation_reasoning
from core.thesis_generator import generate_thesis
from export.pdf_export import create_thesis_pdf

from core.intertext import find_intertext
from viz.intertext_graph import build_intertext_graph

from core.alignment_engine import align_poem
from core.motif_engine import extract_motifs

# =========================
# STREAMLIT CONFIG
# =========================

st.set_page_config(
    page_title="Turkic Literature AI",
    layout="wide"
)

st.title("📊 Turkic Literature AI — Research Cockpit")

# =========================
# INPUT
# =========================

poem = st.text_area("📜 Enter poem for academic analysis")

# =========================
# MAIN PIPELINE
# =========================

if st.button("🚀 Run Full Analysis"):

    if not poem:
        st.warning("Please enter a poem.")
        st.stop()

    try:
        result = foundation_reasoning(poem)

        st.success("Analysis completed")

        # =====================
        # MOTIFS
        # =====================
        st.subheader("🧠 Motifs")
        st.write(result["motifs"])

        # =====================
        # INTERTEXT
        # =====================
        st.subheader("🌐 Intertext Candidates")
        st.write(result["intertext"])

        # =====================
        # ALIGNMENT
        # =====================
        st.subheader("🔗 Cross-Language Alignment")
        st.write(result["alignment"])

        # =====================
        # CITATIONS
        # =====================
        st.subheader("📖 Verified Citations")
        st.write(result["citations"])

    except Exception as e:
        st.error(f"Pipeline error: {e}")

# =========================
# GRAPH VISUALIZATION
# =========================

if st.button("🌐 Intertext Graph"):

    try:
        intertext = find_intertext(poem)
        G = build_intertext_graph(poem, intertext)

        import matplotlib.pyplot as plt
        import networkx as nx

        fig, ax = plt.subplots()

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=800)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Graph error: {e}")

# =========================
# THESIS GENERATOR
# =========================

if st.button("📄 Generate Thesis"):

    try:
        thesis = generate_thesis(poem)
        pdf = create_thesis_pdf(thesis)

        st.success("Thesis generated")

        with open(pdf, "rb") as f:
            st.download_button(
                "⬇ Download Thesis PDF",
                f,
                file_name="thesis.pdf"
            )

    except Exception as e:
        st.error(f"Thesis error: {e}")

# =========================
# SYSTEM HEALTH CHECK
# =========================

if st.button("🧪 System Health Check"):

    checks = {}

    try:
        test = foundation_reasoning("test")
        checks["Foundation Engine"] = True
    except:
        checks["Foundation Engine"] = False

    try:
        extract_motifs("test")
        checks["Motif Engine"] = True
    except:
        checks["Motif Engine"] = False

    try:
        align_poem("test")
        checks["Alignment Engine"] = True
    except:
        checks["Alignment Engine"] = False

    st.write(checks)

    if all(checks.values()):
        st.success("✅ SYSTEM OPERATIONAL")
    else:
        st.error("❌ SYSTEM HAS ISSUES")
