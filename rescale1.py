import cv2 as cv 
img = cv.imread('C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\Photos\\AdobeStock_97589769_Preview.jpeg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


cv.waitKey(0)
cv.destroyAllWindows()

#Reading videos
capture = cv.VideoCapture("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\videos\\AdobeStock_716277764_Video_4K_Preview.mov")
while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) &0xFF==ord('d'):
        break
capture.release()   
cv.destroyAllWindows()
