import cv2 as cv
import numpy as np

# Color of a lake [blue green red]
BGR = np.array([255, 218, 170])
upper = BGR + 10
lower = BGR - 10


# Read an image from disk
# @param {path} the path of the image to read
# @returns {image} the image
def read_image(path):
    return cv.imread(path)


# applies a threshold to an image based on two boundaries
# @param {image} the image to threshold
# @param {Array[int, int, int]} lower threshold in BGR
# @param {Array[int, int, int]} upper threshold in BGR
def find_mask(image):
    return cv.inRange(image, lower, upper)


def find_contours(mask):
    (cnts, hierarchy) = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    print("Found %d black shapes" % (len(cnts)))
    return cnts


# draw contours on an image
# @param {list[[int, int]]} an array of [int, int] points to draw
# @param {image} the image to draw the points on
def show_contours(contours, image):
    for contour in contours:
        cv.drawContours(image, contour, -1, (0, 0, 255), 2)

    # cv.imshow("contours", image)
    # cv.waitKey(0)
    cv.imwrite('output.png', image)


# def get_main_contour(contours):
#     copy = contours.copy()
#     copy.sort(key=len, reverse=True)
#     return copy[0]


if __name__ == "__main__":
    image = read_image("input.png")
    mask = find_mask(image)

    contours = find_contours(mask)
    # main_contour = get_main_contour(contours)
    show_contours([contours], image)

    key = cv.waitKey(0)