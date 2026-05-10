from pyvis.network import Network

def render_graph(G):

    net = Network(height="600px", width="100%", bgcolor="#0e1117", font_color="white")

    net.from_nx(G)

    net.repulsion()

    net.save_graph("graph.html")

    return "graph.html"
