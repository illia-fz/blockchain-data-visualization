import matplotlib.pyplot as plt
import random


def generate_graph_data(n):
    """Generate a list of random edges representing transactions between addresses"""
    return [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in range(n)]


def plot_network(edges):
    """Plot a simple network graph using NetworkX"""
    try:
        import networkx as nx
    except ImportError:
        print("NetworkX is not installed. Please install it to use this feature.")
        return
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title('Sample Blockchain Address Network')
    plt.savefig('address_network.png')
    plt.show()


def main():
    edges = generate_graph_data(10)
    plot_network(edges)


if __name__ == '__main__':
    main()
