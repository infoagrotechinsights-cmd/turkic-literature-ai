import requests

def search_crossref(query, limit=5):

    url = "https://api.crossref.org/works"

    params = {
        "query": query,
        "rows": limit
    }

    r = requests.get(url, params=params)
    data = r.json()

    results = []

    for item in data["message"]["items"]:

        title = item.get("title", [""])[0]
        authors = item.get("author", [])
        year = item.get("published-print", {}).get("date-parts", [[None]])[0][0]

        doi = item.get("DOI", None)

        results.append({
            "title": title,
            "year": year,
            "doi": doi
        })

    return results
