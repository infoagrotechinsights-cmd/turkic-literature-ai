def foundation_reasoning(poem: str):

    try:
        from core.alignment_engine import align_poem
    except Exception:
        align_poem = lambda x: []

    try:
        from core.intertext_engine import analyze_motifs
        motifs = analyze_motifs(poem)
    except Exception:
        motifs = []

    alignment = align_poem(poem)

    return {
        "alignment": alignment,
        "intertext": [],
        "motifs": motifs,
        "citations": [],
        "knowledge_graph": None
    }
