import cv2 as cv 
import numpy as np 

img = cv.imread("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg")

cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])




cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)

merged = cv.merge([b, g, r])




cv.waitKey(0)
cv.destroyAllWindows()
