import csv
import math
from itertools import combinations


def read_points_from_csv(filename):
    points = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            id, x, y = map(float, row[:3])
            points.append((id, x, y))
    return points


def make_triangles(points):
    angles = []
    for triangle in combinations(points, 3):
        id_0, x1, y1 = triangle[0]
        id_1, x2, y2 = triangle[1]
        id_2, x3, y3 = triangle[2]
        angle1 = math.atan2(y2 - y1, x2 - x1)
        angle2 = math.atan2(y3 - y2, x3 - x2)
        angle3 = math.atan2(y1 - y3, x1 - x3)
        angles.append((angle1, angle2, angle3))
    return angles


if __name__ == "__main__":
    filename = "pic1.csv"
    points = read_points_from_csv(filename)
    angles = make_triangles(points)
    print(angles)
