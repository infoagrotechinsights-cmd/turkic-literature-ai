# core/motif_engine.py

def extract_motifs(poem: str):
    """
    Basic motif extractor (stable version)
    """

    motifs = []

    if "kapı" in poem.lower():
        motifs.append({"term": "border / threshold"})

    if "baykuş" in poem.lower():
        motifs.append({"term": "loneliness / night symbol"})

    if "nur" in poem.lower():
        motifs.append({"term": "divine light / mysticism"})

    return motifs
