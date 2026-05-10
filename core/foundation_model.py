from core.language_detector import detect_language
from core.motif_engine import extract_motifs
from core.intertext import find_intertext
from core.alignment_engine import align_poem
from core.crossref_client import search_crossref
from core.citation_verifier import verify_citations


def foundation_reasoning(poem):

    # 1. Language detection
    lang = detect_language(poem)

    # 2. Motif extraction
    motifs = extract_motifs(poem)

    # 3. Intertext graph candidates
    intertext = find_intertext(poem)

    # 4. Cross-language alignment
    alignment = align_poem(poem)

    # 5. Academic grounding
    raw_citations = search_crossref(poem)
    citations = verify_citations(raw_citations)

    # 6. Unified reasoning output
    return {
        "language": lang,
        "motifs": motifs,
        "intertext": intertext,
        "alignment": alignment,
        "citations": citations
    }
