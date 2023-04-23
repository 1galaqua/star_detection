import cv2
import numpy as np
import csv
import math


def pic_to_csv(csv_name, image):
    # Load the image
    img = cv2.imread(image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create ORB detector with custom parameters
    orb = cv2.ORB_create(nfeatures=80, scaleFactor=2, edgeThreshold=90, patchSize=16)

    # Detect keypoints and compute descriptors
    kp, des = orb.detectAndCompute(gray, None)
    kp = duplicate_points(kp)
    # Write the star data to a CSV file
    with open(f'{csv_name}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Star Number', 'x', 'y', 'Brightness', 'Radius'])
        for i, keypoint in enumerate(kp):
            pt = tuple(map(int, keypoint.pt))
            writer.writerow([i + 1, pt[0], pt[1], keypoint.response, keypoint.size])
            cv2.circle(img, (pt[0], pt[1]), 10, (0, 255, 0), thickness=2)

    cv2.namedWindow("Combined Images", cv2.WINDOW_NORMAL)
    resized_img = cv2.resizeWindow("Combined Images", (800, 800))
    cv2.imshow('Combined Images', img)
    # Wait for a key event
    cv2.waitKey(0)
    # Close the window
    cv2.destroyAllWindows()



#filter out nearby stars by radius
def duplicate_points(points):
    for i, pt in enumerate(points):
        for j, com_pt in enumerate(points):
            if i < j:
                pt1 = tuple(map(int, pt.pt))
                pt2 = tuple(map(int, com_pt.pt))
                if abs(pt1[0] - pt2[0]) < 20 or abs(pt1[1] - pt2[1]) < 20:
                    points = points[:j] + points[j + 1:]
                    break
    return points
