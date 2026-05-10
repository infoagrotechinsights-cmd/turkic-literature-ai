# viz/graph.py

import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G):

    fig, ax = plt.subplots(figsize=(12, 8))

    pos = nx.spring_layout(
        G,
        seed=42
    )

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=9,
        ax=ax
    )

    return fig
