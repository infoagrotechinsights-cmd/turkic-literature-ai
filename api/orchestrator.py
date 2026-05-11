from core.foundation_model import foundation_reasoning

# optional modules (SAFE IMPORTS)
try:
    from core.rag_engine import retrieve_context
except Exception:
    def retrieve_context(text):
        return {"context": [], "mode": "disabled"}

try:
    from core.intertext import find_intertext
except Exception:
    def find_intertext(text):
        return []

def run_pipeline(poem: str):

    # =========================
    # 1. FOUNDATION LAYER
    # =========================
    foundation = foundation_reasoning(poem)

    # =========================
    # 2. RAG LAYER
    # =========================
    rag = retrieve_context(poem)

    # =========================
    # 3. INTERTEXT LAYER
    # =========================
    intertext = find_intertext(poem)

    # =========================
    # 4. MOTIF NORMALIZATION
    # =========================
    motifs = foundation.get("motifs", [])

    if not isinstance(motifs, list):
        motifs = []

    # =========================
    # 5. FINAL SAFE OUTPUT
    # =========================
    return {
        "alignment": foundation.get("alignment", []),
        "intertext": intertext,
        "rag_context": rag,
        "motifs": motifs,
        "citations": foundation.get("citations", []),
        "knowledge_graph": foundation.get("knowledge_graph", None)
    }
