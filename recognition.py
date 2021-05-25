import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    lower_red = np.array([0, 0, 255])
    upper_red = np.array([127, 0, 255])
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)


    # Blue color
    lower_blue = np.array([48, 54, 74])
    upper_blue = np.array([179, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    lower_green = np.array([40, 70, 80])
    upper_green = np.array([70, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Yellow color
    lower_yellow = np.array([25, 70, 120])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    if red_mask.any():
        print("red")
    elif blue_mask.any():
        print("blue")
    elif green_mask.any():
        print("green")