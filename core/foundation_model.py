def foundation_reasoning(poem: str):

    from core.alignment_engine import align_poem
    from core.intertext import find_intertext

    alignment = align_poem(poem)
    intertext = find_intertext(poem)

    return {
        "alignment": alignment,
        "intertext": intertext,
        "motifs": [],
        "citations": []
    }
