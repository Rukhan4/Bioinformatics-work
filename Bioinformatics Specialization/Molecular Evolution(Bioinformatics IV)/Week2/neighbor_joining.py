"""
Code Challenge: Implement NeighborJoining.
Input: An integer n, followed by an n x n distance matrix.
Output: An adjacency list for the tree resulting from applying the neighbor-joining algorithm.
"""

import numpy as np
import operator


def neighbor_joining(n, length_matrix, nodes, m):
    graph = dict()
    limb_length = dict()
    if n == 2:
        graph[nodes[0]] = {nodes[1]: length_matrix[0, 1]}
        graph[nodes[1]] = {nodes[0]: length_matrix[1, 0]}
        return(graph)

    total_distance = {}
    for i in range(n):
        total_distance[i] = np.sum(length_matrix[i, :])

    # generate joining matrix
    matrix_star = np.full([n, n], 0, float)  # full nxn matrix with 0.0
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix_star[i, j] = (n - 2) * length_matrix[i, j] - \
                    total_distance[i] - total_distance[j]

    # find minimun value in joining matrix
    min_length = float('Inf')
    for i in range(n):
        for j in range(n):
            if (matrix_star[i, j] != 0) & (matrix_star[i, j] < min_length) & (i < j):
                min_length = matrix_star[i, j]
                min_location = [i, j]
    i_index, j_index = min_location

    i = nodes[i_index]
    j = nodes[j_index]

    # calculate delta for limb length
    delta = (total_distance[i_index] - total_distance[j_index]) / (n - 2)

    limb_length[i_index] = (length_matrix[i_index, j_index] + delta) / 2
    limb_length[j_index] = (length_matrix[i_index, j_index] - delta) / 2

    # make new node
    new_node = m
    m = m + 1

    # update node list
    nodes.append(new_node)
    nodes.remove(i)
    nodes.remove(j)

    # update length matrix
    new_col = []
    for k in range(n):
        new_value = (length_matrix[k, i_index] + length_matrix[k,
                     j_index] - length_matrix[i_index, j_index]) / 2
        new_col.append(new_value)
    length_matrix = np.vstack((length_matrix, np.array(new_col).reshape(1, len(new_col))))
    new_col.append(0)
    length_matrix = np.hstack((length_matrix, np.array(new_col).reshape(len(new_col), 1)))

    length_matrix = np.delete(length_matrix, [i_index, j_index], 0)
    length_matrix = np.delete(length_matrix, [i_index, j_index], 1)

    # iteration
    graph = neighbor_joining(n - 1, length_matrix, nodes, m)

    # update graph
    if new_node in graph:
        graph[new_node][i] = limb_length[i_index]
        graph[new_node][j] = limb_length[j_index]
    else:
        graph[new_node] = {i: limb_length[i_index], j: limb_length[j_index]}
    if i in graph:
        graph[i][new_node] = limb_length[i_index]
    else:
        graph[i] = {new_node: limb_length[i_index]}
    if j in graph:
        graph[j][new_node] = limb_length[j_index]
    else:
        graph[j] = {new_node: limb_length[j_index]}
    print(limb_length)
    print(f'Limblength(i) = {limb_length[0]}')
    return(graph)


if __name__ == "__main__":
    n = 4
    length_matrix = '''0 14 17 17
14 0 7 13
17 7 0 16
17 13 16 0 '''

    nodes = list(range(n))
    m = n
    if type(length_matrix) == str:
        length_matrix = length_matrix.replace('\n', ' ')
        length_matrix = length_matrix.split(' ')
        while '' in length_matrix:
            length_matrix.remove('')
        length_matrix = list(map(int, length_matrix))
        length_matrix = np.array(length_matrix).reshape(n, n)

    tmp = neighbor_joining(n, length_matrix, nodes, m)
    sorted_tmp = dict(sorted(tmp.items(), key=operator.itemgetter(0)))  # Sort keys

    for key1, values1 in sorted_tmp.items():
        for key2, value2 in values1.items():
            print(str(key1) + '->' + str(key2) + ':' + str(value2))
