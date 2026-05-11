from core.foundation_model import foundation_reasoning
from core.rag_engine import retrieve_academic_context
from core.citation_verifier import search_crossref
from core.intertext import find_intertext


class Orchestrator:

    def run(self, poem: str):

        intertext = find_intertext(poem)

        foundation = foundation_reasoning(poem, intertext)

        rag = retrieve_academic_context(poem)

        citations = search_crossref(poem)

        return {
            "intertext": intertext,
            "analysis": foundation,
            "rag": rag,
            "citations": citations
        }
