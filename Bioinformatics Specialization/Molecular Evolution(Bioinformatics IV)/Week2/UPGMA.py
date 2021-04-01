""" Implement UPGMA.

Input: An integer n followed by a space separated n x n distance matrix.
Output: An adjacency list for the ultrametric tree returned by UPGMA.
Edge weights should be accurate to two decimal places
    """

import numpy as np
import operator
from math import ceil


def UPGMA(n, length_matrix):
    if type(length_matrix) == str:
        length_matrix = length_matrix.replace('\n', ' ')
        length_matrix = length_matrix.split(' ')
        while '' in length_matrix:
            length_matrix.remove('')
        length_matrix = list(map(int, length_matrix))
        length_matrix = np.array(length_matrix).reshape(n, n)

    clusters = list(range(n))
    ages = dict()
    graph = dict()
    n_node_cluster = dict()

    for node in clusters:
        ages[node] = 0
        n_node_cluster[node] = 1

    while len(clusters) != 1:

        n = length_matrix.shape[0]

        # find minimun length
        min_length = float('Inf')
        for i in range(n):
            for j in range(n):
                if (length_matrix[i, j] != 0) & (length_matrix[i, j] < min_length) & (i < j):
                    min_length = length_matrix[i, j]
                    min_location = [i, j]

        i_index, j_index = min_location

        i = clusters[i_index]
        j = clusters[j_index]

        # make new cluster
        new_cluster = max(clusters) + 1

        # update new cluster's n_node
        n_node_cluster[new_cluster] = n_node_cluster[i] + n_node_cluster[j]

        # update cluster list
        clusters.remove(i)
        clusters.remove(j)
        clusters.append(new_cluster)

        # update ages
        ages[new_cluster] = length_matrix[i_index, j_index] / 2

        # add new cluster to graph
        if new_cluster in graph:
            graph[new_cluster][i] = ages[new_cluster] - ages[i]
            graph[new_cluster][j] = ages[new_cluster] - ages[j]
        else:
            graph[new_cluster] = {i: (ages[new_cluster] - ages[i]),
                                  j: (ages[new_cluster] - ages[j])}
        if i in graph:
            graph[i][new_cluster] = ages[new_cluster] - ages[i]
        else:
            graph[i] = {new_cluster: (ages[new_cluster] - ages[i])}
        if j in graph:
            graph[j][new_cluster] = ages[new_cluster] - ages[j]
        else:
            graph[j] = {new_cluster: (ages[new_cluster] - ages[j])}

        new_col = []
        for vi, vj in zip(length_matrix[:, i_index], length_matrix[:, j_index]):
            if (vi * vj) != 0:
                new_value = (vi * n_node_cluster[i] + vj * n_node_cluster[j]
                             ) / (n_node_cluster[i] + n_node_cluster[j])
                new_col.append(new_value)

        # update matrix
        length_matrix = np.delete(length_matrix, [i_index, j_index], 0)
        length_matrix = np.delete(length_matrix, [i_index, j_index], 1)

        length_matrix = np.vstack((length_matrix, np.array(new_col).reshape(1, len(new_col))))
        new_col.append(0)
        length_matrix = np.hstack((length_matrix, np.array(new_col).reshape(len(new_col), 1)))

    cluster_str = ''
    cluster_str = clusters[0]
    print(f'The number of clusters is: {cluster_str}')
    return(graph)


"""
Code below is for rounding to 2 decimal places
"""
# def rounding_2_decimals(graph):
#     for x in graph:
#         for k, v in x.items():
#             v = round(v, 3)
#             x[k] = v
#     return


# n = 4
# length_matrix = '''0 20 17 11
#     20 0 20 13
#     17 20 0 10
#     11 13 10 0'''


# class TwoDec(float):
#     def __repr__(self):
#         return "%.2f" % self


# def roundingVals_to_2Deci(y, ceil=ceil, TwoDec=TwoDec):
#     for d in y:
#         for k, v in d.iteritems():
#             d[k] = TwoDec(ceil(v*100)/100)


# res = UPGMA(n, length_matrix)
# print(roundingVals_to_2Deci(graph, ceil=ceil, TwoDec=TwoDec)


if __name__ == "__main__":
    n = 4
    length_matrix = """0 20 17 11
    20 0 20 13
    17 20 0 10
    11 13 10 0"""

    tmp = UPGMA(n, length_matrix)
    sorted_tmp = dict(sorted(tmp.items(), key=operator.itemgetter(0)))  # Sort keys

    for key1, values1 in sorted_tmp.items():
        for key2, value2 in values1.items():
            print(str(key1) + "->" + str(key2) + ":" + str(value2))
