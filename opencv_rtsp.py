import numpy as np
import cv2 as cv
import sys

cap = cv.VideoCapture("rtspsrc location=rtsp://128.224.176.161:8554/test latency=0 ! rtph264depay ! decodebin ! videoconvert ! appsink")

if cap.isOpened() == False:
    print "VideoCapture Failed!"
    sys.exit(1)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',gray)
    cv.imshow('ori',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
