import networkx as nx

def build_intertext_graph(poem):

    G = nx.Graph()

    # Basit motif sözlüğü (MVP)
    motif_map = {
        "bayqush": ["Şehriyar", "exile motif"],
        "kafes": ["political oppression", "freedom"],
        "nur": ["Sufism", "Ibn Arabi"],
        "qelb": ["love poetry", "Fuzuli"]
    }

    for motif, links in motif_map.items():
        if motif in poem.lower():

            for link in links:

                if link in ["Şehriyar", "Fuzuli", "Yunus Emre"]:
                    G.add_edge("Poem", link)
                else:
                    G.add_edge("Poem", link)
                    G.add_edge(link, "Concept")

    return G
