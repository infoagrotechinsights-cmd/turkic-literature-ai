from core.alignment_engine import align_poem
from core.intertext import find_intertext
from core.rag_engine import retrieve_academic_context


def foundation_reasoning(poem: str):

    alignment = align_poem(poem)
    intertext = find_intertext(poem)
    rag = retrieve_academic_context(poem)

    return {
        "alignment": alignment,
        "intertext": intertext,
        "rag": rag,
        "citations": []
    }
