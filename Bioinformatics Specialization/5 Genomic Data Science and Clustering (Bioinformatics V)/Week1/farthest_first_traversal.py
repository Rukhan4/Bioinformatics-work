""" 
Code Challenge: Implement the FarthestFirstTraversal clustering heuristic.
Input: Integers k and m followed by a set of points Data in m-dimensional space.
Output: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k),
where the first point from Data is chosen as the first center to initialize the algorithm.
"""
import math


def euclidean_distance(point1, point2):
    sum_square_delta = 0
    for v, w in zip(point1, point2):
        sum_square_delta = sum_square_delta + (v - w)**2
    distance = math.sqrt(sum_square_delta)
    return(distance)


def farthest_first_traversal(k, m, points_data):
    if type(points_data) == str:
        points = []
        points_data = points_data.split('\n')
        for point_data in points_data:
            point_data = point_data.split(' ')
            point_data = list(map(float, point_data))
            points.append(point_data)

    cluster_centers = [points[0]]

    while len(cluster_centers) != k:

        max_distance_centers_point = -float('Inf')

        for point in points:
            min_distance_center_point = float('Inf')

            for center in cluster_centers:
                distance = euclidean_distance(center, point)
                if distance < min_distance_center_point:
                    min_distance_center_point = distance

            if min_distance_center_point > max_distance_centers_point:
                max_distance_centers_point = min_distance_center_point
                max_point = point

        cluster_centers.append(max_point)

    return(cluster_centers)

# points_data = '''0.0 0.0
# 5.0 5.0
# 0.0 5.0
# 1.0 1.0
# 2.0 2.0
# 3.0 3.0
# 1.0 2.0'''
#k,m = 3,2


if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\farthestfirsttraversal.txt", "r") as file:
        integers = []
        for val in file.readline().split(' '):
            integers.append(val)
        k = int(integers[0])
        m = int(integers[1].replace('\n', ''))

        points_data = file.read().strip()

    for point in farthest_first_traversal(k, m, points_data):
        print(*point)
