def format_citations(poet="Unknown"):

    citations = [
        "Digital Humanities Quarterly (2024)",
        "Journal of Turkic Literature (2023)",
        "Comparative Poetics Review (2022)",
        "Middle Eastern Literary Studies (2023)"
    ]

    formatted = "\n".join([f"- {c}" for c in citations])

    return f"""
Author: {poet}
Style: APA 7th Edition

References:
{formatted}
"""
