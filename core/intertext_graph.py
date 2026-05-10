import networkx as nx

def build_intertext_graph(center_poem, related_poems):

    G = nx.Graph()

    G.add_node(
        "CENTER",
        label="Original Poem",
        type="source"
    )

    for i, p in enumerate(related_poems):

        node_id = f"P{i}"

        motif_labels = [m["term"] for m in p.get("motifs", [])]

        G.add_node(
            node_id,
            label=p["author"],
            score=p["score"],
            motifs=",".join(motif_labels),
            shared=p.get("shared_structure", 0)
        )

        G.add_edge(
            "CENTER",
            node_id,
            weight=p["score"] + p.get("shared_structure", 0) * 0.2,
            relation="intertextual_similarity"
        )

    return G
