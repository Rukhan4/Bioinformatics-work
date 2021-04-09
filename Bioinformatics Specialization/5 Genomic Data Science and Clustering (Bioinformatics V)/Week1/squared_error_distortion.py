""" 
Code Challenge: Solve the Squared Error Distortion Problem.

Input: Integers k and m, followed by a set of centers Centers and a set of points Data.
Output: The squared error distortion Distortion(Data, Centers).
"""
from farthest_first_traversal import euclidean_distance


def squared_error_distortion(points_data, centers_data):
    if type(points_data) == str:
        points = []
        points_data = points_data.split('\n')
        for point_data in points_data:
            point_data = point_data.split(' ')
            point_data = list(map(float, point_data))
            points.append(point_data)
    else:
        points = points_data

    if type(centers_data) == str:
        centers = []
        centers_data = centers_data.split('\n')
        for center_data in centers_data:
            center_data = center_data.split(' ')
            center_data = list(map(float, center_data))
            centers.append(center_data)
    else:
        centers = centers_data

    distortion = 0

    for point in points:
        min_distance_center_point = float('Inf')
        for center in centers:
            distance = euclidean_distance(center, point)
            if distance < min_distance_center_point:
                min_distance_center_point = distance

        distortion = distortion + min_distance_center_point**2

    distortion = distortion / len(points)

    return(distortion)


if __name__ == "__main__":
    centers_data = '''8.3 3.0
9.8 6.7
2.2 3.0
1.1 8.1'''

    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\squarederrordistortion.txt", "r") as file:
        points_data = file.read().strip()

    print(squared_error_distortion(points_data, centers_data))
