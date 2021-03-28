'''
Code Challenge: Solve the Limb Length Problem.
Input: An integer n, followed by an integer j between 0 and n - 1, followed by a space-separated additive distance matrix D (whose elements are integers).
Output: The limb length of the leaf in Tree(D) corresponding to row j of this distance matrix (use 0-based indexing).
'''
import numpy as np


def limb_length(j, length_matrix):
    if type(length_matrix) == str:
        length_matrix = length_matrix.replace('\n', ' ')
        length_matrix = length_matrix.split(' ')
        length_matrix = list(map(int, length_matrix))
        length_matrix = np.array(length_matrix).reshape(n, n)

    min_length = float('Inf')
    for i in range(length_matrix.shape[0]):
        if i != j:
            for k in range(length_matrix.shape[0]):
                if (k != j) & (k != i):
                    # Allowing for linear time complexity since Tree(D) is simple - tree with no nodes of degree 2
                    length = (length_matrix[i, j] + length_matrix[j, k] - length_matrix[i, k]) / 2
                    if length < min_length:
                        min_length = int(length)

    return(min_length)


if __name__ == "__main__":
    n = 4
    j = 2  # LimbLength answer
    length_matrix = '''0 20 9 11
20 0 17 11
9 17 0 8
11 11 8 0'''

    print(limb_length(j, length_matrix))
