import cv2 as cv 
import numpy as np 


img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



lap = cv.Laplacian(gray, cv.CV_64F)

lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

    
cv.waitKey(0)