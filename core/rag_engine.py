def retrieve_context(text: str):

    keywords = {
        "kristeva": "intertextuality theory",
        "bakhtin": "dialogism",
        "metinlerarasılık": "literary theory",
        "sembol": "semiotics",
        "tasavvuf": "mysticism"
    }

    context = []

    lower = text.lower()

    for k, v in keywords.items():
        if k in lower:
            context.append({
                "concept": k,
                "theory": v,
                "relevance": 0.8
            })

    return {
        "query": text,
        "context": context,
        "mode": "semantic_stub_rag"
    }
