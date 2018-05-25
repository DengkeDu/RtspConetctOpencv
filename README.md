# opencv connected to Gstreamer rtsp server

### NOTE1
1. Gstreamer rtsp server run on raspberrypi0-wifi
2. opencv run on a ubuntu 16.04 machine

### opencv build with gstreamer
```
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

#### depends
https://docs.opencv.org/3.4.1/d7/d9f/tutorial_linux_install.html

we should also install the following:
```
gstreamer1.0
gstreamer1.0-libav
gstreamer1.0-python
gstreamer1.0-rtsp-server
gstreamer1.0-rtsp-server-dev
gstreamer1.0-plugins-bad
gstreamer1.0-plugins-good
libgstreamer-plugins-base1.0-0
libgstreamer-plugins-base1.0-dev
libgstreamer-plugins-good1.0-0
libgstreamer-plugins-good1.0-dev
libgstreamer1.0-0
libgstreamer1.0-dev
libgstreamer-plugins-bad1.0-0
libgstreamer-plugins-bad1.0-dev
```

#### building
```
cd opencv
mkdir build && cd build
cmake .. -DOPENCV_EXTRA_MODULES_PATH=path_to_opencv_contrib
make 
sudo make install
```

maker sure the WITH_GSTREAMER:BOOL=ON in CMakeCache.txt(automate create)

### raspberrypi side
first console:
```
raspivid -n -t 0 -hf -fps 20 -w 300 -h 300 -o - | gst-launch-1.0 fdsrc ! \
    h264parse ! gdppay ! tcpserversink host=127.0.0.1 port=5001
```
second console:
```
./test-launch "( tcpclientsrc host=127.0.0.1 port=5001 ! gdpdepay ! rtph264pay pt=96 name=pay0 )"
```

### opencv side
1. run the build.sh script
or
2. mkdir build && cd build && cmake .. && make
or
3. python opencv_rtsp.py
or
4. gst-launch-1.0 rtspsrc location="rtsp://rtsp_server_ip:8554/test" latency=0 ! rtph264depay ! decodebin ! videoconvert ! ximagesink

### NOTE2
the ip in opencv_rtsp.py and opencv_rtsp.cpp, you need to replace you raspberrypi's ip.

### audio
```
pactl list | grep -A2 'Source #' | grep 'Name: ' | cut -d" " -f2
gst-launch-1.0 pulsesrc device="alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono" ! audioconvert ! autoaudiosink
```

