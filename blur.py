import cv2 as cv 


img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_625571921_Preview.jpeg')


#averaging 
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)

#Gaussian Blur 
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('GaussianBlur', gauss)

#Median Blur 
median = cv.medianBlur(img, 3)
cv.imshow('MedianBLur', median)

#bilateral 
bilateral = cv.bilateralFilter(img, 5, 15, 15)



cv.waitKey(0)


