import csv
import math
from itertools import combinations
import math
import cv2


def angle_between_points(A, B, C):
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
    magnitude_AB = math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
    magnitude_BC = math.sqrt((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2)
    angle = math.acos(dot_product / (magnitude_AB * magnitude_BC))
    return angle


def read_points_from_csv(filename):
    points = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            id, x, y = map(float, row[:3])
            points.append((id, x, y))
    return points


def calculate_angle(x1, y1, x2, y2, x3, y3):
    # Calculate distances between the three points
    a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Use the law of cosines to calculate the angle opposite to side a
    angle_in_radians = math.acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))

    # Convert from radians to degrees
    angle_in_degrees = math.degrees(angle_in_radians)

    return angle_in_degrees


def make_triangles(points):
    angles = []

    for triangle in combinations(points, 3):
        id_0, x1, y1 = triangle[0]
        id_1, x2, y2 = triangle[1]
        id_2, x3, y3 = triangle[2]
        angle1 = int(calculate_angle(x2, y2, x3, y3, x1, y1) * 10) / 10
        angle2 = int(calculate_angle(x3, y3, x1, y1, x2, y2) * 10) / 10
        angle3 = (int(180 - angle1 - angle2) * 10) / 10
        angles.append([angle1, angle2, angle3, id_0, id_1, id_2])
    return angles


def compare(list1, list2):
    matches = []
    matches2 = []
    for tuple1 in list1:
        for tuple2 in list2:
            if tuple1[:2] == tuple2[:2]:
                matches.append(tuple1)
                matches2.append(tuple2)
    if len(matches) == 0:
        return "no result"
    return matches, matches2



if __name__ == "__main__":
    filename = "pic1.csv"
    points = read_points_from_csv(filename)
    angles = make_triangles(points)
    # print(angles)

    filename2 = "pic2.csv"
    points2 = read_points_from_csv(filename2)
    angles2 = make_triangles(points2)
    # print(angles2)
    matches = compare(angles, angles2)
    img = cv2.imread("pic1.csv")
    
    list1, list2 = compare(angles, angles2)
