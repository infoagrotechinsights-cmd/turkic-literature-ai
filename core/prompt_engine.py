def build_prompt(poem: str, context: str = None):

    base = f"""
You are a PhD-level Turkic literature scholar.

TASK:
- Translate poem
- Analyze themes
- Identify intertextuality
- Do not hallucinate citations

POEM:
{poem}
"""

    if context:
        base += f"\n\nRAG CONTEXT:\n{context}"

    return base
