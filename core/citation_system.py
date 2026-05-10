def format_citation(item):

    return {
        "title": item.get("title", ""),
        "doi": item.get("DOI", ""),
        "year": item.get("year", ""),
        "style": "APA 7"
    }
