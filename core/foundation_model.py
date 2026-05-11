from core.alignment_engine import align_poem
from core.intertext import find_intertext


def foundation_reasoning(poem: str):

    alignment = align_poem(poem)
    intertext = find_intertext(poem)

    motifs = extract_motifs(intertext)

    return {
        "alignment": alignment,
        "intertext": intertext,
        "motifs": motifs,
        "citations": []
    }


def extract_motifs(intertext):

    motifs = []

    for item in intertext:

        motifs.append({
            "term": item.get("term"),
            "type": item.get("type")
        })

    return motifs
