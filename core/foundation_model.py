# core/foundation_model.py

def foundation_reasoning(poem: str):
    """
    Main research pipeline controller
    """

    # lazy imports (CRITICAL)
    from core.alignment_engine import align_poem
    from core.intertext import find_intertext
    from core.motif_engine import extract_motifs

    alignment = align_poem(poem)
    intertext = find_intertext(poem)
    motifs = extract_motifs(poem)

    return {
        "alignment": alignment,
        "intertext": intertext,
        "motifs": motifs,
        "citations": []
    }
