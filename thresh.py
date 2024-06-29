import cv2 as cv 

img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_220757428_Preview.jpeg')

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)