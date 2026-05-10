from core.crossref_client import search_crossref

def verify_citations(text):

    results = search_crossref(text, limit=3)

    verified = []

    for r in results:

        if r["title"]:

            verified.append(
                f"{r['title']} ({r['year']}) DOI: {r['doi']}"
            )

    if not verified:
        return "❌ GERÇEK KAYNAK BULUNAMADI (HALLÜSİNASYON ENGELLENDİ)"

    return verified
