"""
Expectation maximization algorithm for soft k-means clustering
Input: Integers k and m, followed by a stiffness parameter β, followed by a set of points Data in m-dimensional space.
Output: A set Centers consisting of k points (centers) resulting from applying the expectation maximization algorithm for soft
    k-means clustering. Select the first k points from Data as the first centers for the algorithm and run the algorithm for 100
    E-steps and 100 M-steps.
"""
import numpy as np
import math


def euclidean_distance(point1, point2):
    sum_square_delta = 0
    for v, w in zip(point1, point2):
        sum_square_delta = sum_square_delta + (v - w)**2
    distance = math.sqrt(sum_square_delta)
    return(distance)


def E_Steps(centers, points, beta):
    hidden_matrix = np.full((points.shape[0], centers.shape[0]), 0, float)

    for i in range(points.shape[0]):
        for j in range(centers.shape[0]):
            hidden_matrix[i, j] = np.exp(-1 * beta * euclidean_distance(points[i], centers[j]))
        hidden_matrix[i, :] = hidden_matrix[i, :] / np.sum(hidden_matrix[i, :])

    return(hidden_matrix)


def M_Steps(hidden_matrix, points):
    centers = np.full((hidden_matrix.shape[1], points.shape[1]), 0, float)

    for i in range(hidden_matrix.shape[1]):
        for j in range(points.shape[1]):
            centers[i, j] = np.dot(hidden_matrix[:, i], points[:, j]) / np.sum(hidden_matrix[:, i])

    return(centers)


def soft_k_means(k, m, beta, points_data):
    if type(points_data) == str:
        points = []
        points_data = points_data.split('\n')
        for point_data in points_data:
            point_data = point_data.split(' ')
            point_data = list(map(float, point_data))
            points.append(point_data)
    else:
        points = points_data

    points = np.array(points).reshape(len(points_data), m)
    centers = points[: k]

    for _ in range(100):
        hidden_matrix = E_Steps(centers, points, beta)
        centers = M_Steps(hidden_matrix, points)

    return(centers)


k, m = 2, 2
beta = 2.7
points_data = '''1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9'''

for center in soft_k_means(k, m, beta, points_data):
    print(*center)
