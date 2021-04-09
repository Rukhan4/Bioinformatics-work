""" 
Code Challenge: Implement the Lloyd algorithm for k-means clustering.

Input: Integers k and m followed by a set of points Data in m-dimensional space.
Output: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers, 
where the first k points from Data are selected as the first k centers.  
"""

import numpy as np
from squared_error_distortion import squared_error_distortion
from farthest_first_traversal import euclidean_distance


def center_of_gravity(points):
    n_col = points.shape[1]
    n_row = points.shape[0]
    center = []
    for j in range(n_col):
        col = points[:, j]
        center.append(np.sum(col) / n_row)
    return(center)


def lloyd_k_means(k, m, points_data):
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
    error = squared_error_distortion(points, centers)

    while True:

        cluster_belonging = []
        for point in points:
            min_distance_center_point = float('Inf')

            for j in range(len(centers)):
                distance = euclidean_distance(centers[j], point)
                if distance < min_distance_center_point:
                    min_distance_center_point = distance
                    min_center = int(j)

            cluster_belonging.append(min_center)
        cluster_belonging = np.array(cluster_belonging)

        current_centers = []

        for j in range(len(centers)):

            current_cluster_points = points[cluster_belonging == j]
            current_centers.append(center_of_gravity(current_cluster_points))

        current_error = squared_error_distortion(points, current_centers)

        if abs(current_error - error) < 0.000001:
            return(current_centers)
        else:

            centers = current_centers
            error = current_error


# k, m = 2, 2
# points_data = '''1.3 1.1
# 1.3 0.2
# 0.6 2.8
# 3.0 3.2
# 1.2 0.7
# 1.4 1.6
# 1.2 1.0
# 1.2 1.1
# 0.6 1.5
# 1.8 2.6
# 1.2 1.3
# 1.2 1.0
# 0.0 1.9'''

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\lloyd.txt", "r") as file:
        integers = []
        for val in file.readline().split(' '):
            integers.append(val)
        k = int(integers[0])
        m = int(integers[1].replace('\n', ''))

        points_data = file.read().strip()

    for centers in lloyd_k_means(k, m, points_data):
        print(*centers)
