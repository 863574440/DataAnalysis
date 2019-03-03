import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def draw_graph(G):
    # G = nx.Graph()
    # G.add_edge('A', 'B', weight=4)
    # G.add_edge('B', 'D', weight=2)
    # G.add_edge('A', 'C', weight=3)
    # G.add_edge('C', 'D', weight=5)
    # G.add_edge('A', 'D', weight=10)
    # for u, v, d in G.edges(data=True):
    #     print(u, v, d['weight'])

    # edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
    # fixed_position = {'A': [0.55072989, 0.00426975], 'B': [1., 0.], 'D': [0.38252302, 0.10520343],
    #                   'C': [0., 0.09481996]}  # 每个点在坐标轴中的位置
    # pos = nx.spring_layout(G, pos=fixed_position)  # 获取结点的位置,每次点的位置都是随机的
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # 绘制图中边的权重
    # # print(edge_labels)
    nx.draw_networkx(G)
    plt.show()


graph = nx.DiGraph()
edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'D'), ('C', 'A'), ('D', 'B'), ('D', 'C')]

graph.add_edges_from(edges)
page_rank = nx.pagerank(graph, alpha=0.85)
print(page_rank)
draw_graph(graph)
