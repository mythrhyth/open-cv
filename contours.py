import cv2 as cv 
import numpy as np

img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg')

cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

cv.imshow('Gray', gray)



canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found')


cv.waitKey(0)
