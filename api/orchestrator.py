def run_pipeline(poem: str):

    # =========================
    # SAFE IMPORT LAYER
    # =========================
    try:
        from core.foundation_model import foundation_reasoning
    except Exception as e:
        return {"error": f"foundation_model load failed: {e}"}

    try:
        from core.rag_engine import retrieve_context
    except Exception:
        retrieve_context = lambda x: {"context": [], "mode": "disabled"}

    try:
        from core.intertext import find_intertext
    except Exception:
        find_intertext = lambda x: []

    # =========================
    # EXECUTION LAYER
    # =========================
    try:
        foundation = foundation_reasoning(poem)
    except Exception as e:
        foundation = {
            "alignment": [],
            "intertext": [],
            "motifs": [],
            "citations": [],
            "error": str(e)
        }

    rag = retrieve_context(poem)
    intertext = find_intertext(poem)

    # =========================
    # NORMALIZATION LAYER
    # =========================
    motifs = foundation.get("motifs", [])
    if not isinstance(motifs, list):
        motifs = []

    return {
        "alignment": foundation.get("alignment", []),
        "intertext": intertext,
        "rag_context": rag,
        "motifs": motifs,
        "citations": foundation.get("citations", []),
        "knowledge_graph": foundation.get("knowledge_graph", None)
    }
