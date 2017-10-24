# Real-Time-Color-Detector
This is a Real Time Color Detector/Scanner that is used to identify colors that are showing in the video .

## How it works
* First, it starts off the webcam for video capture
* Now we extract frame by frame from the image and do analysis on it
* Now we have lower and upper bounds for colors
* Since we got the color values now we will compare it with each frame we will get from the video
* As the pixels of color value matches with certain pixels on the frame, we will draw a rectangle over there at ROI (Region of Interest)
* Hence as soon as we got a frame and color is recognized there will be a new rectangle formed.
