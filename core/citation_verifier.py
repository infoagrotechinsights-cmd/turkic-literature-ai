def verify_citations(citations):
    """
    Sadece gerçek DOI olanları geçirir.
    Fake / boş / hallucinated kaynakları siler.
    """

    verified = []

    for c in citations:

        if not isinstance(c, dict):
            continue

        doi = c.get("doi", None)
        title = c.get("title", "")

        # 🚨 kritik filter
        if not doi:
            continue

        if len(title) < 5:
            continue

        verified.append({
            "title": title,
            "doi": doi,
            "year": c.get("year"),
            "authors": c.get("authors", [])
        })

    return verified
