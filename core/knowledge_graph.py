# core/knowledge_graph.py

import networkx as nx


def build_knowledge_graph(intertexts):

    G = nx.Graph()

    # CENTRAL NODE
    G.add_node(
        "Poem",
        type="main"
    )

    for item in intertexts:

        keyword = item["keyword"]

        theory = item["theory"]

        tradition = item["tradition"]

        # =====================
        # MAIN CONNECTIONS
        # =====================

        G.add_node(
            keyword,
            type="motif"
        )

        G.add_edge(
            "Poem",
            keyword
        )

        G.add_node(
            theory,
            type="theory"
        )

        G.add_edge(
            keyword,
            theory
        )

        G.add_node(
            tradition,
            type="tradition"
        )

        G.add_edge(
            keyword,
            tradition
        )

        # =====================
        # AUTHORS
        # =====================

        for author in item["related_authors"]:

            G.add_node(
                author,
                type="author"
            )

            G.add_edge(
                keyword,
                author
            )

    return G
