
'''
Code Challenge: Implement additive phylogeny to solve the Distance-Based Phylogeny Problem.
Input: An integer n followed by a space-separated n x n distance matrix.
Output: A weighted adjacency list for the simple tree fitting this matrix.
'''
from limb_length import limb_length
import copy
import numpy as np
import operator


def attached_limb(length_matrix, j):
    for i in range(length_matrix.shape[0]):
        for k in range(length_matrix.shape[0]):
            if (i != j) & (k != j):
                if length_matrix[i, k] == length_matrix[i, j - 1] + length_matrix[j - 1, k]:
                    return(i, k)


def find_path(nodes, current, final, path, visited, final_path):
    path = path + [current]
    visited.append(current)
    neighbor_nodes = nodes[current].keys()
    if current == final:
        final_path.extend(path)
        return

    unvisited_neighbor_nodes = set(neighbor_nodes) - set(visited)
    if len(unvisited_neighbor_nodes) == 0:
        return

    for unvisited_neighbor_node in list(unvisited_neighbor_nodes):
        find_path(nodes, int(unvisited_neighbor_node), final, path, visited, final_path)

    return final_path


def add_to_graph(length_matrix, nodes, n, m, i, k, x):
    visited = []
    final_path = []

    i_k_path = find_path(nodes, i, k, [], visited, final_path)
    total_length = 0

    for index in range(len(i_k_path) - 1):
        current_node = i_k_path[index]
        next_node = i_k_path[index + 1]
        length_between = nodes[current_node][next_node]
        total_length = total_length + length_between

        if total_length == x:
            limb_length_curr = limb_length(n, length_matrix)
            nodes[next_node][n] = limb_length_curr
            nodes[n] = {next_node: limb_length_curr}
            return nodes

        elif total_length > x:
            length1 = x - (total_length - length_between)
            length2 = total_length - x

            limb_length_curr = limb_length(n, length_matrix)

            nodes[current_node].pop(next_node)
            nodes[next_node].pop(current_node)

            nodes[current_node][m[0]] = length1
            nodes[next_node][m[0]] = length2
            nodes[m[0]] = {current_node: length1, next_node: length2}

            nodes[m[0]][n] = limb_length_curr
            nodes[n] = {m[0]: limb_length_curr}
            m[0] = m[0] + 1
            return nodes
    return nodes


def additive_phylogeny(length_matrix, n, m):
    if n == 1:
        nodes = {}
        nodes[1] = {0: length_matrix[0, 1]}
        nodes[0] = {1: length_matrix[0, 1]}
        return nodes

    limb_length_curr = limb_length(n, length_matrix)

    sub_matrix = copy.deepcopy(length_matrix)

    for j in range(n):

        sub_matrix[j, n] = sub_matrix[j, n] - limb_length_curr
        sub_matrix[n, j] = sub_matrix[j, n]

    (i, k) = attached_limb(sub_matrix, n)

    x = sub_matrix[i, n]

    sub_matrix = sub_matrix[: -1, : -1]

    nodes = additive_phylogeny(sub_matrix, n-1, m)

    nodes = add_to_graph(length_matrix, nodes, n, m, i, k, x)
    return nodes


if __name__ == "__main__":
    n = 5
    length_matrix = '''0 11 10 9 15
11 0 3 12 18
10 3 0 11 17
9 12 11 0 8
15 18 17 8 0'''
    if type(length_matrix) == str:
        length_matrix = length_matrix.replace('\n', ' ')
        length_matrix = length_matrix.split(' ')
        length_matrix = list(map(int, length_matrix))
        length_matrix = np.array(length_matrix).reshape(n, n)

    tmp = additive_phylogeny(length_matrix, n - 1, [n])
    sorted_tmp = dict(sorted(tmp.items(), key=operator.itemgetter(0)))  # Sort keys
    for key1, values1 in sorted_tmp.items():
        for key2, value2 in values1.items():
            print(str(key1) + '->' + str(key2) + ':' + str(value2))
