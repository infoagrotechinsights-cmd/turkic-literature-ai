from core.alignment_engine import align_poem
from core.intertext import find_intertext
from core.rag_engine import retrieve_context
from core.citation_verifier import verify_citations

def foundation_reasoning(poem: str):

    alignment = align_poem(poem)
    intertext = find_intertext(poem)

    rag_context = retrieve_context(poem)
    citations = verify_citations(poem)

    motifs = [
        {
            "term": item["term"],
            "type": item.get("type", "unknown"),
            "score": item.get("score", 0.0)
        }
        for item in intertext
    ]

    return {
        "alignment": alignment,
        "intertext": intertext,
        "rag_context": rag_context,
        "motifs": motifs,
        "citations": citations
    }
