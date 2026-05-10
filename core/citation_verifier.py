# core/citation_verifier.py

import requests


CROSSREF_API = "https://api.crossref.org/works"


def search_crossref(query: str):

    try:

        url = f"{CROSSREF_API}?query={query}&rows=3"

        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            return []

        data = response.json()

        items = data["message"]["items"]

        results = []

        for item in items:

            title = item.get("title", ["Unknown"])[0]

            authors = []

            for a in item.get("author", []):
                given = a.get("given", "")
                family = a.get("family", "")
                authors.append(f"{given} {family}")

            year = "n.d."

            if "published-print" in item:
                year = item["published-print"]["date-parts"][0][0]

            doi = item.get("DOI", "")

            journal = item.get(
                "container-title",
                ["Unknown Journal"]
            )[0]

            apa = build_apa(
                authors,
                year,
                title,
                journal,
                doi
            )

            results.append({

                "title": title,
                "authors": authors,
                "year": year,
                "journal": journal,
                "doi": doi,
                "apa": apa,
                "verified": True

            })

        return results

    except Exception as e:

        return [{
            "verified": False,
            "error": str(e)
        }]


def build_apa(authors, year, title, journal, doi):

    if authors:
        author_text = ", ".join(authors)
    else:
        author_text = "Unknown Author"

    return f"{author_text} ({year}). {title}. {journal}. https://doi.org/{doi}"


def verify_sources(intertext_results):

    verified_sources = []

    for item in intertext_results:

        keyword = item["keyword"]

        query = f"{keyword} Turkish literature"

        results = search_crossref(query)

        verified_sources.extend(results)

    return verified_sources
