import cv2 as cv 
# img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_97589769_Preview.jpeg')
# cv.imshow('Cat', img)



# cv.waitKey(0)
def resizeFrame(resize, )

capture = cv.VideoCapture("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\videos\\AdobeStock_716277764_Video_4K_Preview.mov")
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) &0xFF==ord('d'):
        break
    
cv.waitKey(0)
capture.release()   
cv.destroyAllWindows()
