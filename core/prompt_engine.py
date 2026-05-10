def build_prompt(poem, context=None, citations=None):
    prompt = f"""
You are a PhD-level Turkic literature AI.

POEM:
{poem}
"""

    if context:
        prompt += f"\nCONTEXT:\n{context}\n"

    if citations:
        prompt += f"\nCITATIONS:\n{citations}\n"

    return prompt
