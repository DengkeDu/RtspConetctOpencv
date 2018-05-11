#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
int main(void)
{     
    /*cv::VideoCapture cap("rtspsrc location=rtsp://128.224.176.180:8554/test ! decodebin ! videoconvert ! appsink name=sink caps=video/x-raw,format=BGR sync=false");*/
    cv::VideoCapture cap("rtspsrc location=rtsp://128.224.176.161:8554/test ! rtph264depay ! decodebin ! videoconvert ! appsink");
    if( !cap.isOpened() )
    {
	std::cout << "Not good, open camera failed" << std::endl;
        return 0;
    }
    std::cout << " Open IP camera successfully!" <<std::endl;
    cv::Mat frame;
    while(true)
    {
	cap >> frame;
        cv::imshow("Frame", frame);
        cv::waitKey(1);
    }
    return 0;
}

