import re

# basit ama genişletilebilir motif ontology
MOTIF_DICTIONARY = {
    "kapı": ["threshold", "border", "transition"],
    "qapı": ["threshold", "border", "transition"],
    "sarp": ["difficulty", "barrier", "liminality"],
    "baykuş": ["isolation", "ruin", "melancholy"],
    "nur": ["light", "divine", "spirituality"],
    "darlık": ["oppression", "constraint", "existential_pressure"],
    "sınır": ["border", "political_space", "division"]
}

def extract_motifs(text):

    text_lower = text.lower()

    found = []

    for word, categories in MOTIF_DICTIONARY.items():

        if word in text_lower:

            found.append({
                "term": word,
                "categories": categories,
                "frequency": len(re.findall(word, text_lower))
            })

    return found
