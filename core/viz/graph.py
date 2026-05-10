import networkx as nx

def build_graph(data):

    G = nx.Graph()

    for item in data:

        poet = item.get("poet", "Unknown")
        influence = item.get("influence", "Unknown")

        G.add_node(poet)
        G.add_node(influence)
        G.add_edge(poet, influence)

    return G
