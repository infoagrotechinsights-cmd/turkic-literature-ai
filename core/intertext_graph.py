import networkx as nx

def build_cross_language_graph(center_poem, aligned_poems):

    G = nx.Graph()

    G.add_node(
        "CENTER",
        label="Original Poem",
        language="source"
    )

    for i, p in enumerate(aligned_poems):

        node_id = f"L{i}"

        G.add_node(
            node_id,
            label=p["language"],
            text_preview=p["text"][:60],
            score=p["alignment_score"]
        )

        G.add_edge(
            "CENTER",
            node_id,
            weight=p["alignment_score"],
            relation="cross_language_alignment"
        )

    return G
