import networkx as nx
import matplotlib.pyplot as plt

def create_graph(nodes):

    G = nx.Graph()

    G.add_node("Research Paper")

    for node in nodes.keys():
        G.add_node(node)
        G.add_edge("Research Paper", node)

    return G


def draw_graph(G):

    fig, ax = plt.subplots(figsize=(8, 5))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        ax=ax
    )

    return fig