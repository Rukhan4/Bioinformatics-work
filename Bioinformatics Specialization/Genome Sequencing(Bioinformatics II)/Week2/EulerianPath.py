# Eulerian Path Problem - returns the eulerian path of a edges from the adjacency list of a directed edges
from EulerianCycle import EulerianCycle
import operator


with open('C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/eulerianpath.txt', 'r') as file:
    graph = dict((line.strip().split(' -> ') for line in file))
    for key in graph:
        graph[key] = graph[key].split(',')


def get_balance(adj_list):
    balance = {}
    for start in adj_list.keys():
        if not balance.get(start):
            balance[start] = 0
        for end in adj_list[start]:
            balance[start] -= 1
            if balance.get(end):
                balance[end] += 1
            else:
                balance[end] = 1
    return balance


def EulerianPath(graph):
    path = []
    stack = []
    balance = get_balance(graph)
    stack.append(min(balance.items(), key=operator.itemgetter(1))[0])
    while len(stack) != 0:
        start = stack[-1]
        if graph.get(start):
            end = graph[start][0]
            stack.append(end)
            graph[start].remove(end)
        else:
            path.append(stack.pop())

    num_edges = sum((len(v) for v in graph.values()))
    if num_edges == 0:
        return list(reversed(path))
    return []


path = EulerianPath(graph)
print(" -> ".join(map(str, path)))
