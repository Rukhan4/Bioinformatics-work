"""
Compute the distances between leaves in a weighted tree.

Input:  An integer n followed by the adjacency list of a weighted tree with n leaves.
Output: An n x n matrix (di,j), where di,j is the length of the path between leaves i and j.
"""

import numpy as np


def distance_matrix(n, adjacency_list):
    if type(adjacency_list) == str:
        adjacency_list = adjacency_list.split('\n')

    graph = dict()
    graph_weight = dict()
    for adjacency in adjacency_list:
        adjacency = adjacency.split(':')
        graph_weight[adjacency[0]] = int(adjacency[1])
        adjacency = adjacency[0].split('->')
        adjacency[0], adjacency[1] = int(adjacency[0]), int(adjacency[1])
        if adjacency[0] in graph:
            graph[adjacency[0]].append(adjacency[1])
        else:
            graph[adjacency[0]] = [(adjacency[1])]

    length_matrix = np.full([n, n], 0, int)

    for from_ in range(n):
        weight_row = [0] * (max(graph.keys()) + 1)
        froms = [from_]

        while len(froms) != 0:

            next_froms = []
            for node in froms:
                tos = graph[node]

                for to in tos:
                    if to != from_:
                        if (to not in range(n)) & (weight_row[to] == 0):
                            next_froms.append(to)

                        graph_weight_key = str(node) + '->' + str(to)
                        weight = graph_weight[graph_weight_key]
                        weight_row[to] = weight_row[node] + weight

            froms = next_froms
        length_matrix[from_, :] = weight_row[: n]

    return(length_matrix)


if __name__ == "__main__":
    n = 4
    adjacency_list = '''0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6'''

    nparray = distance_matrix(n, adjacency_list)
    for x in nparray:
        print(*x)

    # with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\distancematrix.txt", 'r') as input_file:
    #     adj_unformatted = []
    #     string = ''
    #     for line in input_file:
    #         adj_unformatted.append(line.rstrip())
    #     for matrix_piece in adj_unformatted:
    #         adjacency_list += matrix_piece+'\n'
    #    print(adjacency_list)
    # print(distance_matrix(n, adjacency_list))
