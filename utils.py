#file for image processing
import numpy as np
import cv2 as cv
import constant
from constant import center


def processimage(image):
    image = list(image)
    image = np.array(image, np.uint8)
    image = image.reshape(constant.res[1], constant.res[1], 3)
    gimage = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(gimage, 20, 225, 0)
    # calculate centroid using moments
    M = cv.moments(thresh)
    if M["m00"] == 0.0:
        cx = 0.0
        cy = center
    else:
        cx = float(M["m10"] / M["m00"])
        cy = float(M["m01"] / M["m00"])
    return cy