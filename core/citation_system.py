import random

def generate_citation(poet="Unknown"):

    sources = [
        "Journal of Turkic Studies (2023)",
        "Digital Humanities Quarterly (2024)",
        "Comparative Literature Review (2022)",
        "Middle Eastern Poetics Journal (2023)"
    ]

    return {
        "author": poet,
        "source": random.choice(sources),
        "style": "APA 7th"
    }
