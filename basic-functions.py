import cv2 as cv 

img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_220757428_Preview.jpeg')

#graying image
#cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow('Gray', gray)



blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)

#cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny', canny)

#dilating the images 
dilated = cv.dilate(canny, (7, 7), iterations = 3)
#cv.imshow('dilated', dilated)

#erode the image 
eroded = cv.erode(dilated, (7, 7), iterations = 3)
#cv.imshow('erode', eroded)

resized = cv.resize(img, (500, 500))
#cv.imshow('resize', resized)

cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)