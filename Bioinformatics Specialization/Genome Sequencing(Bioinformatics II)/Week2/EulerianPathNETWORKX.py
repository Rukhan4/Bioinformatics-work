# Eulerian Path -returns the eulerian path of a edges from the adjacency list of a directed edges
# USES NETWORKX

import networkx as nx

with open('C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/eulerianpath.txt', 'r') as file:
    graph = dict((line.strip().split(' -> ') for line in file))
    for key in graph:
        graph[key] = graph[key].split(',')

file.close()


def EulerianPath(graph):
    G = nx.DiGraph()
    nodes = [i for i in graph]
    edges = []
    for i in graph:
        for j in graph[i]:
            edges.append([i, j])

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    EulPath = list(nx.eulerian_path(G))

    path = ''
    path += '%s' % (EulPath[0][0])
    for i in range(len(EulPath)):
        path += '->%s' % (EulPath[i][1])

    return path


ans = EulerianPath(graph)
print(" -> ".join(map(str, ans)))
with open('C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/eulerianpathanswer.txt', 'w') as file:
    file.write(EulerianPath(graph))

file.close()
