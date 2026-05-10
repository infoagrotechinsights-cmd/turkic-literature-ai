def verify_citation(text):

    fake_indicators = [
        "unknown journal",
        "AI generated source",
        "fictional study"
    ]

    for f in fake_indicators:
        if f in text.lower():
            return False

    return True
