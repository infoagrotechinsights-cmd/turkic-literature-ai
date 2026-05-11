from core.alignment_engine import align_poem
from core.intertext import find_intertext


def foundation_reasoning(poem: str):

    alignment = align_poem(poem)
    intertext = find_intertext(poem)

    motifs = [
        {"term": i.get("term"), "type": i.get("type")}
        for i in intertext
    ]

    return {
        "alignment": alignment,
        "intertext": intertext,
        "motifs": motifs,
        "citations": []
    }
