from core.llm_engine import ask_gpt

def generate_review(topic):

    prompt = f"""
Write an academic literature review about:

{topic}

Include:
- major scholars
- historical evolution
- Turkic + Persian + Ottoman connections
- citations style APA 7
"""

    return ask_gpt(prompt)
