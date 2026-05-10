def build_prompt(poem, context=None, citations=None):

    prompt = f"""
You are a PhD-level computational literature researcher.

TASK:
- Translate poem if needed
- Perform academic analysis
- Extract intertextual relations
- Avoid hallucinated sources

POEM:
{poem}
"""

    if context:
        prompt += f"""

CONTEXT (RAG + Foundation Model):
{context}
"""

    if citations:
        prompt += f"""

VERIFIED ACADEMIC SOURCES (DO NOT MODIFY OR INVENT):
{citations}
"""

    prompt += """

RULES:
- Use only provided citations
- If citations are empty, explicitly say: "No verified sources found"
- Maintain academic tone (APA style where applicable)
"""

    return prompt
