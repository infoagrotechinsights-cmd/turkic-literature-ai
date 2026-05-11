def retrieve_context(text: str):
    """
    Simple RAG fallback engine (production-safe stub)
    """

    # şimdilik lightweight semantic context
    keywords = [
        "Kristeva",
        "Bakhtin",
        "metinlerarasılık",
        "sembol",
        "tasavvuf",
        "modernizm"
    ]

    context = []

    lower = text.lower()

    for k in keywords:
        if k.lower() in lower:
            context.append({
                "source": "internal_knowledge_base",
                "concept": k,
                "relevance": 0.75
            })

    return {
        "query": text,
        "context": context,
        "mode": "fallback_rag"
    }
