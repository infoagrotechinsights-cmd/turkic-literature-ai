def build_prompt(poem, mode="academic"):

    base_prompts = {

        "academic": """
You are a PhD-level literature scholar.
Analyze the poem academically.

Focus:
- themes
- symbols
- cultural context
- literary devices
- historical background
""",

        "intertextuality": """
Detect intertextual references in Turkic literature.
Compare with:
- Fuzuli
- Nazim Hikmet
- Şehriyar
- Yunus Emre
- Persian poetic tradition
""",

        "thesis": """
Write as a PhD thesis section:

Include:
- introduction
- theoretical framework
- analysis
- conclusion
- academic tone
"""
    }

    return f"""
{base_prompts.get(mode)}

POEM:
{poem}
"""
