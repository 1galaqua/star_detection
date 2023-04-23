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

    try:
        # Use the law of cosines to calculate the angle opposite to side a
        angle_in_radians = math.acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))
    except:
        angle_in_radians = 1

    # Convert from radians to degrees
    angle_in_degrees = math.degrees(angle_in_radians)

    return angle_in_degrees

#make triangle by three angles
#return list
def make_triangles(points):
    angles = []
    for triangle in combinations(points, 3):
        id_0, x1, y1 = triangle[0]
        id_1, x2, y2 = triangle[1]
        id_2, x3, y3 = triangle[2]
        angle1 = int(calculate_angle(x2, y2, x3, y3, x1, y1) * 10) / 10
        angle2 = int(calculate_angle(x3, y3, x1, y1, x2, y2) * 10) / 10
        angle3 = (int(180 - angle1 - angle2) * 10) / 10
        if angle1 > 5 and angle2 > 5 and angle3 > 5:
            angles.append([angle1, angle2, angle3, int(id_0), int(id_1), int(id_2)])
    return angles

#finde similar triangles
def compare(list1, list2):
    matches = []
    matches2 = []
    for tuple1 in list1:
        for tuple2 in list2:
            if tuple1[:2] == tuple2[:2]:
                matches.append(tuple1)
                matches2.append(tuple2)
    return matches, matches2

#illustration the stars by data of similar triangle
def draw_lines(list_of_matches, csv_name, image):
    img = cv2.imread(image)
    for i in list_of_matches:
        with open(f'{csv_name}.csv', 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            id1, id2, id3 = i[3:]
            for row in csvreader:
                if row[0] == str(id1):
                    point_id1 = (int(row[1]), int(row[2]))
                if row[0] == str(id2):
                    point_id2 = (int(row[1]), int(row[2]))
                if row[0] == str(id3):
                    point_id3 = (int(row[1]), int(row[2]))
            if point_id3 and point_id2 and point_id1:
                # cv2.line(img, point_id1, point_id2, (0, 255, 0), 3)
                # cv2.line(img, point_id2, point_id3, (0, 255, 0), 3)
                # cv2.line(img, point_id3, point_id1, (0, 255, 0), 3)
                # Define the radius of the circle
                radius = 10
                # Define the color of the circle (in BGR format)
                color = (0, 0, 255)  # Red
                cv2.circle(img, point_id3, radius, color, thickness=2)
                cv2.circle(img, point_id2, radius, color, thickness=2)
                cv2.circle(img, point_id1, radius, color, thickness=2)
    return img
