def build_prompt(poem, context=None, citations=None):

    prompt = f"""
You are a PhD-level Turkic literature scholar.

RULES (CRITICAL):
- Do NOT invent citations
- Only use VERIFIED SOURCES provided
- If no citation exists, say "no verified academic source found"

TASK:
1. Translate poem
2. Thematic analysis
3. Intertextuality
4. Historical context

POEM:
{poem}
"""

    if context:
        prompt += f"""

RAG CONTEXT:
{context}
"""

    if citations:
        prompt += f"""

VERIFIED ACADEMIC SOURCES (DO NOT MODIFY):
{citations}
"""

    return prompt
