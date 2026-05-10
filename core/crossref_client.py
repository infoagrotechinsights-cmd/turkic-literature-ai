import requests

CROSSREF_URL = "https://api.crossref.org/works"

def search_crossref(query, limit=5):
    try:
        params = {
            "query": query,
            "rows": limit
        }

        r = requests.get(CROSSREF_URL, params=params, timeout=10)
        data = r.json()

        items = data.get("message", {}).get("items", [])

        results = []

        for item in items:
            title = item.get("title", [""])[0]
            doi = item.get("DOI", None)
            year = item.get("issued", {}).get("date-parts", [[None]])[0][0]
            author = item.get("author", [])

            authors = []
            for a in author:
                name = f"{a.get('family','')} {a.get('given','')}"
                authors.append(name)

            if doi:
                results.append({
                    "title": title,
                    "doi": doi,
                    "year": year,
                    "authors": authors,
                    "source": "crossref"
                })

        return results

    except Exception as e:
        return [{"error": str(e)}]
