import networkx as nx

def build_graph(similar_poems):

    G = nx.Graph()

    G.add_node("INPUT_POEM")

    for i, poem in enumerate(similar_poems):

        node = f"POEM_{i}"

        G.add_node(node)

        G.add_edge("INPUT_POEM", node)

    return G
