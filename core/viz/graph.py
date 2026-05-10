import networkx as nx

def build_graph(data):

    G = nx.Graph()

    for item in data:

        G.add_node(item["poet"])
        G.add_node(item["influence"])
        G.add_edge(item["poet"], item["influence"])

    return G
