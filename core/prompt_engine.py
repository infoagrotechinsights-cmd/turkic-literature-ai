def build_prompt(poem, context=None, citations=None):
    
    prompt = f"""
You are a PhD-level Turkic literature research assistant.

TASK:
- Academic analysis of poem
- Intertextual interpretation
- Thematic extraction

POEM:
{poem}
"""

    if context:
        prompt += f"""

CONTEXT:
{context}
"""

    if citations:
        prompt += f"""

VERIFIED ACADEMIC SOURCES:
{citations}
"""

    return prompt
