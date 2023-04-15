import cv2
import numpy as np
import csv


def pic_to_csv(csv_name, image):
    # Load the image
    img = cv2.imread(image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create ORB detector with custom parameters
    orb = cv2.ORB_create(nfeatures=60, scaleFactor=3, edgeThreshold=90, patchSize=16)

    # Detect keypoints and compute descriptors
    kp, des = orb.detectAndCompute(gray, None)

    # Write the star data to a CSV file
    with open(f'{csv_name}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Star Number', 'x', 'y', 'Brightness', 'Radius'])
        for i, keypoint in enumerate(kp):
            pt = tuple(map(int, keypoint.pt))
            writer.writerow([i + 1, pt[0], pt[1], keypoint.response, keypoint.size])
            cv2.circle(img, pt, 5, (0, 0, 255), -1)

    # Show the image with marked stars
    cv2.namedWindow("Image 1", cv2.WINDOW_NORMAL)
    resized_img = cv2.resizeWindow("Image 1", (800, 800))

    # Display the results
    cv2.imshow("Image 1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
