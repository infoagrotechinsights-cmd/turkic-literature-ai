import networkx as nx

def build_intertext_graph(center_poem, related_poems):

    G = nx.Graph()

    # merkez node
    G.add_node("CENTER", label="Original Poem", type="source")

    for i, p in enumerate(related_poems):

        node_id = f"P{i}"

        # node
        G.add_node(
            node_id,
            label=p["author"],
            score=p["score"],
            motifs=",".join(p.get("motifs", []))
        )

        # edge (KRİTİK UPGRADE)
        G.add_edge(
            "CENTER",
            node_id,
            weight=p["score"],
            relation=p["type"]
        )

    return G
