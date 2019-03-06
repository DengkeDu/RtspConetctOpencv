import numpy as np
import cv2 as cv
import sys

cap = cv.VideoCapture("rtspsrc location=rtsp://127.0.0.1:8554/test latency=0 ! rtph264depay ! decodebin ! videoconvert ! appsink")

if cap.isOpened() == False:
    print "VideoCapture Failed!"
    sys.exit(1)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('ori',frame)
    c = cv.waitKey(1)
    if c == ord('q'):
        break
    elif c == ord('p'):
        print "Saved picture image.png"
        cv.imwrite('image.png',frame)

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
