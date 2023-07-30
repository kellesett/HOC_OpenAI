import cv2 as cv
import numpy as np


def multiple_obj_detection(haystack_img, needle_img):
    # highlight all founded examples
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    cv.imshow('Result', result)
    cv.waitKey()

    threshold = 0.95
    location = np.where(result >= threshold)

    needle_h = needle_img.shape[1]
    needle_w = needle_img.shape[0]

    for pt in zip(location[1], location[0]):
        top_left = pt
        bottom_right = (pt[0] + needle_h, pt[1] + needle_w)

        cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0),  thickness=2)

    cv.imshow('Result', haystack_img)
    cv.waitKey()


if __name__ == "__main__":
    image = cv.imread('../images/img_2.png')
    template = cv.imread('../images/chests/chest_of_chests.png')

    multiple_obj_detection(image, template)
