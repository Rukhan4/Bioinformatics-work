"""
Code Challenge: Implement HierarchicalClustering.
Input: An integer n, followed by an n x n distance matrix.
Output: The result of applying HierarchicalClustering to this distance matrix (using Davg),
with each newly created cluster listed on each line.
"""
import numpy as np


def hierarchical_clustering(n, distance_matrix):
    if type(distance_matrix) == str:
        distance_matrix = distance_matrix.replace('\n', ' ')
        distance_matrix = distance_matrix.split(' ')
        while '' in distance_matrix:
            distance_matrix.remove('')
        distance_matrix = list(map(float, distance_matrix))
        distance_matrix = np.array(distance_matrix).reshape(n, n)

    clusters = []
    for i in range(n):
        clusters.append([i + 1])

    while len(clusters) != 1:
        n = distance_matrix.shape[0]

        # find minimun length
        min_length = float('Inf')
        for i in range(n):
            for j in range(n):
                if (distance_matrix[i, j] != 0) & (distance_matrix[i, j] <= min_length) & (i < j):
                    min_length = distance_matrix[i, j]
                    min_location = [i, j]

        i_index, j_index = min_location

        i = clusters[i_index]
        j = clusters[j_index]

        # make new cluster
        new_cluster = i + j

        # print new cluster
        tmp_print = new_cluster
        tmp_print = list(map(str, tmp_print))
        print(' '.join(tmp_print))

        # make new colomn
        new_col = []
        for vi, vj in zip(distance_matrix[:, i_index], distance_matrix[:, j_index]):
            if (vi * vj) != 0:
                new_value = (vi * len(clusters[i_index]) + vj * len(clusters[j_index])
                             ) / (len(clusters[i_index]) + len(clusters[j_index]))
                new_col.append(new_value)

        # update matrix
        distance_matrix = np.delete(distance_matrix, [i_index, j_index], 0)
        distance_matrix = np.delete(distance_matrix, [i_index, j_index], 1)

        distance_matrix = np.vstack((distance_matrix, np.array(new_col).reshape(1, len(new_col))))
        new_col.append(0)
        distance_matrix = np.hstack((distance_matrix, np.array(new_col).reshape(len(new_col), 1)))

        # update cluster
        clusters.remove(i)
        clusters.remove(j)
        clusters.append(new_cluster)

    # return min_length/2


# n = 4
# distance_matrix = '''0 20 9 11
# 20 0 17 11
# 9 17 0 8
# 11 11 8 0'''

#print(hierarchical_clustering(n, distance_matrix))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\hierarchicalclustering.txt", "r") as file:
        n = int(file.readline())
        distance_matrix = file.read()

    print(hierarchical_clustering(n, distance_matrix))
