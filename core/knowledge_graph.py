import networkx as nx

G = nx.Graph()


def build_graph(intertext):

    G.clear()

    for item in intertext:

        term = item.get("term")
        typ = item.get("type")
        weight = item.get("weight", 0.5)

        if term and typ:

            # 🔥 REAL RELATIONSHIP EDGE
            G.add_edge(term, typ, weight=weight)

    return G


def get_graph():
    return G
