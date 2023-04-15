import cv2
import numpy as np
import csv
import pandas as pd
# Load the images
img1 = cv2.imread('stars_images/image1.jpeg')
img2 = cv2.imread('stars_images/image2.jpeg')

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Detect keypoints and compute descriptors using ORB detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Match descriptors using brute force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:500000], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Show the matched stars on the original images
matched_kp1 = [kp1[match.queryIdx] for match in matches[:500000]]
matched_kp2 = [kp2[match.trainIdx] for match in matches[:500000]]
# Write the matched star data to a CSV file
with open('matched_stars.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Star Number', 'Image 1 x', 'Image 1 y', 'Image 2 x', 'Image 2 y', 'Brightness', 'Radius'])
    for i, (kp1, kp2) in enumerate(zip(matched_kp1, matched_kp2)):
        pt1 = tuple(map(int, kp1.pt))
        pt2 = tuple(map(int, kp2.pt))
        writer.writerow([i+1, pt1[0], pt1[1], pt2[0], pt2[1], kp1.response, kp1.size])
        cv2.circle(img1, pt1, 5, (0, 0, 255), -1)
        cv2.circle(img2, pt2, 5, (0, 0, 255), -1)
        cv2.line(img_matches, pt1, (pt2[0] + img1.shape[1], pt2[1]), (0, 255, 0), thickness=1)

# Write the image 1 star data to a CSV file
with open('image1_stars.csv', mode='w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(['Star Number', 'Image 1 x', 'Image 1 y', 'Brightness', 'Radius'])
    for i, (kp1, kp2) in enumerate(zip(matched_kp1, matched_kp2)):
        pt1 = tuple(map(int, kp1.pt))
        writer.writerow([i+1, pt1[0], pt1[1], kp1.response, kp1.size])

# Write the image 2 star data to a CSV file
with open('image2_stars.csv', mode='w', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(['Star Number', 'Image 2 x', 'Image 2 y', 'Brightness', 'Radius'])
    for i, (kp1, kp2) in enumerate(zip(matched_kp1, matched_kp2)):
        pt2 = tuple(map(int, kp2.pt))
        writer.writerow([i+1, pt2[0], pt2[1], kp2.response, kp2.size])


# Resize the image
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
resized_img = cv2.resizeWindow("Resized_Window", (600, 600))
resized_img1 = cv2.resize(img1, (500, 500))
resized_img2 = cv2.resize(img2, (500, 500))
# Display the results

cv2.imshow("Resized_Window", img_matches)

cv2.imshow('Image 1', resized_img1)
cv2.imshow('Image 2', resized_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
