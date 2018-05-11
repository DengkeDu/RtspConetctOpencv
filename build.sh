#!/bin/sh

#gcc opencv_rtsp.cpp -o opencv_rtsp -lopencv_core -lstdc++
g++ -I/usr/local/include -L/usr/local/lib opencv_rtsp.cpp -o opencv_rtsp -lopencv_videoio -lopencv_core -lopencv_shape -lopencv_highgui -lopencv_ximgproc

