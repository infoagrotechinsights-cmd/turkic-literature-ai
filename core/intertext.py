# core/intertext.py

def find_intertext(poem: str):
    """
    Simple intertext detection placeholder
    """

    keywords = ["sarp", "kapı", "baykuş", "nur"]

    found = [k for k in keywords if k in poem.lower()]

    return [
        {"term": f"intertext:{k}", "confidence": 0.7}
        for k in found
    ]
