import streamlit as st

# ONLY SAFE IMPORT
from core.foundation_model import foundation_reasoning

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Turkic Literature AI",
    layout="wide"
)

st.title("📚 Turkic Literature AI")
st.markdown("### Academic Research Cockpit")

# =========================
# INPUT
# =========================

poem = st.text_area(
    "📜 Paste poem or literary text",
    height=250
)

# =========================
# ANALYSIS BUTTON
# =========================

if st.button("🚀 Run Analysis"):

    if not poem.strip():
        st.warning("Please enter a poem.")
        st.stop()

    try:

        # =========================
        # MAIN PIPELINE
        # =========================

        result = foundation_reasoning(poem)

        st.success("✅ Analysis completed")

        # =========================
        # ALIGNMENT
        # =========================

        st.subheader("🔗 Alignment")

        if "alignment" in result:
            st.json(result["alignment"])
        else:
            st.warning("No alignment result.")

        # =========================
        # INTERTEXT
        # =========================

        st.subheader("🌐 Intertext Relations")

        if "intertext" in result:
            st.json(result["intertext"])
        else:
            st.warning("No intertext data.")

        # =========================
        # MOTIFS
        # =========================

        st.subheader("🧠 Motifs")

        if "motifs" in result:
            st.json(result["motifs"])
        else:
            st.warning("No motif analysis.")

        # =========================
        # CITATIONS
        # =========================

        st.subheader("📖 Citations")

        if "citations" in result:
            st.json(result["citations"])
        else:
            st.warning("No citations found.")

    except Exception as e:

        st.error("❌ SYSTEM ERROR")
        st.code(str(e))

# =========================
# HEALTH CHECK
# =========================

st.divider()

if st.button("🧪 System Health Check"):

    checks = {}

    # foundation model
    try:
        foundation_reasoning("test")
        checks["foundation_model"] = "OK"
    except Exception as e:
        checks["foundation_model"] = f"ERROR: {e}"

    st.subheader("System Status")
    st.json(checks)

    if all(v == "OK" for v in checks.values()):
        st.success("✅ SYSTEM OPERATIONAL")
    else:
        st.error("❌ SYSTEM HAS ERRORS")
