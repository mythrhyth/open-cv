import cv2 as cv 

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\opencv\\videos\\AdobeStock_716277764_Video_4K_Preview.mov")
while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()   
cv.destroyAllWindows()