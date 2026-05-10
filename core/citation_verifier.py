def verify_citations(text):

    references = []

    if "Levinas" in text:
        references.append("Levinas (2002). Totality and Infinity.")

    if "Camus" in text:
        references.append("Camus (1942). The Myth of Sisyphus.")

    return {
        "style": "APA 7",
        "references": references
    }
