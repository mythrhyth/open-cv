import cv2 as cv 
import numpy as np


img = cv.imread("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg")

cv.imshow('cats', img)


blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 100, 255, -1)

cv.imshow('Mask', mask)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(mask, rectangle)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked image', masked)

weird_shaped_mask = cv.bitwise_and(img, img, mask = weird_shape)
cv.imshow('weird_shaped_mask', weird_shaped_mask)



cv.waitKey(0)






