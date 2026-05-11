def render_academic(result):

    motifs = result.get("motifs", [])

    if not motifs:
        return "No semantic motifs detected."

    output = "📚 Academic Analysis (PhD Level)\n\n"

    output += "2. Metinlerarasılık Katmanı\n"

    for m in motifs:
        output += f"""
{m['term']} → {m['type']} (score: {round(m['score'],2)})
Metinlerarasılık açısından bu yapı kültürel sembol üretir.
"""

    output += "\n3. Kuramsal Arka Plan\nKristeva + Bakhtin semantic layer aktif\n"

    return output
