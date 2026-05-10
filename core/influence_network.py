import networkx as nx

def build_influence_network(poets_data):

    G = nx.Graph()

    for poet in poets_data:

        G.add_node(poet["name"])

        for influence in poet.get("influences", []):

            G.add_edge(poet["name"], influence)

    return G
