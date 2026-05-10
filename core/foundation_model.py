from core.llm_engine import ask_gpt

def analyze_poem_multilingual(text):

    prompt = f"""
Sen Turkic Literature Foundation Model'sin.

Görev:
1. Azerice/Türkçe/Farsça metni çöz
2. Modern Türkçeye çevir
3. Akademik analiz üret
4. Şairler arası etkileri çıkar

Metin:
{text}

Çıktı:
- Çeviri
- Tematik analiz
- Tarihsel bağlam
- Metinlerarasılık
"""

    return ask_gpt(prompt)
