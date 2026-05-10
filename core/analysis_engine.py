from core.llm_engine import ask_gpt

def analyze_poem(poem, analysis_type):

    prompt = f"""
    Analyze this poem with {analysis_type} perspective.

    Poem:
    {poem}
    """

    return ask_gpt(prompt)
