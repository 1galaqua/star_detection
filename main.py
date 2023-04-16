from pic_to_csv import pic_to_csv
from triangels import read_points_from_csv


if __name__ == "__main__":
    pic1 = pic_to_csv("pic1", 'stars_images/image1.jpeg')
    pic2 = pic_to_csv("pic2", 'stars_images/image2.jpeg')
    list_pic1 = read_points_from_csv(pic1)
    list_pic2 = read_points_from_csv(pic2)
