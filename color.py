import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
while True :
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    kernal = np.ones((5, 5), "uint8")

    # For Red Color
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red = cv2.inRange(hsv, red_lower, red_upper)
    red = cv2.dilate(red, kernal)
    res = cv2.bitwise_and(frame, frame, mask=red)
    (_, contours, _) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Red Color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # For Blue Color
    blue_lower = np.array([99, 115, 150], np.uint8)
    blue_upper = np.array([110, 255, 255], np.uint8)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    blue = cv2.dilate(blue, kernal)
    res = cv2.bitwise_and(frame, frame, mask=blue)
    (_, contours, _) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Blue Color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    # For Yellow Color
    yellow_lower = np.array([22, 60, 200], np.uint8)
    yellow_upper = np.array([60, 255, 255], np.uint8)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    yellow = cv2.dilate(yellow, kernal)
    res = cv2.bitwise_and(frame, frame, mask=yellow)
    (_, contours, _) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Yellow Color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255))

    cv2.imshow('Real Time Color Detector' , frame)

    if cv2.waitKey(0) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()




