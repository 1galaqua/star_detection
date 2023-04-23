from pic_to_csv import pic_to_csv
from match import read_points_from_csv, make_triangles, compare, draw_lines
import time
import cv2

if __name__ == "__main__":
    image1 = 'boaz/fr1.jpg'
    image2 = 'boaz/fr2.jpg'

    pic_to_csv("pic1", image1)
    pic_to_csv("pic2", image2)
    filename = "pic1.csv"
    points = read_points_from_csv(filename)
    triangles = make_triangles(points)


    filename2 = "pic2.csv"
    points2 = read_points_from_csv(filename2)
    triangles2 = make_triangles(points2)

    list1, list2 = compare(triangles, triangles2)
    img1 = draw_lines(list1, "pic1", image1)
    img2 = draw_lines(list2, "pic2", image2)

    # Resize the images to have the same height
    cv2.namedWindow("Combined Images", cv2.WINDOW_NORMAL)
    resized_img = cv2.resizeWindow("Combined Images", (800, 800))
    cv2.namedWindow("C", cv2.WINDOW_NORMAL)
    resized_img = cv2.resizeWindow("C", (800, 800))
    # Concatenate the images horizontally
    # combined_img = cv2.hconcat([img1, img2])

    # Show the combined image in a window
    cv2.imshow('Combined Images', img1)
    cv2.imshow('C', img2)

    # Wait for a key event
    cv2.waitKey(0)

    # Close the window
    cv2.destroyAllWindows()
    # time.sleep(50)
