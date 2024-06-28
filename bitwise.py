import cv2 as cv 
import numpy as np 

blank = np.zeros((400, 400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(),(30, 30), (370, 370), 255, -1)

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise and --> intersecting regions

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#bitwise or --> non-intersecting regions


bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR --> non-intersecting regions

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise xnor --> 

bitwise_xnor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XNOR', bitwise_xnor)

#bitwise not --> it just inverts black to white and white to black

cv.waitKey(0)