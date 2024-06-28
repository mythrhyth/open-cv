import cv2 as cv 
import numpy as np


img = cv.imread("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg")

cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

mask = cv.circle(blank, (img.shape[1]//2 + 100, img.shape[0]//2 + 100, 100, 255, -1))

cv.imshow('Mask', mask)

rectangle= cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shap


