import cv2 as cv
import numpy as np 

img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg')

cv.imshow('cat', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)

cv.waitKey(0)
