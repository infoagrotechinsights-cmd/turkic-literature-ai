from core.alignment_engine import align_poem
from core.intertext import find_intertext


def foundation_reasoning(poem: str):

    alignment = align_poem(poem)

    intertext = find_intertext(poem)

    return {
        "alignment": alignment,
        "intertext": intertext,
        "motifs": extract_motifs(intertext),
        "citations": []
    }


def extract_motifs(intertext):
    return [
        {"term": i.get("term"), "type": i.get("type")}
        for i in intertext
    ]
