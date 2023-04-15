import cv2
import numpy as np
import csv
import pandas as pd
# Load the images
img1 = cv2.imread('stars_images/image1.jpeg')


# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Detect keypoints and compute descriptors using ORB detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(gray1, None)


# Match descriptors using brute force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des1)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw
img_matches = cv2.drawMatches(img1, kp1, img1, kp1, matches[:500000], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
matched_kp1 = [kp1[match.queryIdx] for match in matches[:500000]]

# Write the image 1 star data to a CSV file
with open('image11111_stars.csv', mode='w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(['Star Number', 'Image 1 x', 'Image 1 y', 'Brightness', 'Radius'])
    for i, (kp1) in enumerate(matched_kp1):
        pt1 = tuple(map(int, kp1.pt))
        cv2.circle(img1, pt1, 5, (0, 0, 255), -1)
        writer.writerow([i+1, pt1[0], pt1[1], kp1.response, kp1.size])



# Resize the image
cv2.namedWindow("Image 1", cv2.WINDOW_NORMAL)
resized_img = cv2.resizeWindow("Image 1", (800, 800))


# Display the results



cv2.imshow("Image 1", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
