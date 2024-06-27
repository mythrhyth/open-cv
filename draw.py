import cv2 as cv 
import numpy as np 

blank = np.zeros((500, 500, 3), dtype = 'uint8')

#show box

blank[200:300, 300:400] = 0, 255, 0 

#cv.imshow('Green', blank)

#show rectangle
cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness = -2)
# cv.imshow('Green', blank)

#show circle

cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0, 0, 255), thickness = -1)

#cv.imshow('circle', blank)

#show line

cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness = 3)

#cv.imshow('line', blank)

#put fonts 
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness = 1)
cv.imshow('text', blank)



cv.waitKey(0)





