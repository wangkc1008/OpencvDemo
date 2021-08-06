"""
Create Date: 2021/8/5
Create Time: 18:22
Author: wangkc
"""
import cv2
import numpy as np
from ImageStack import stackImages

frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)

my_color = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]

my_color_values = [[51, 153, 255],
                   [255, 0, 255],
                   [0, 255, 0]]

my_points = []


def find_color(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    i = 0
    new_points = []
    for index, color in enumerate(my_color):
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(img_hsv, lower, upper)
        x, y = find_contours(mask)
        if x != 0 and y != 0:
            new_points.append([x, y, i])
        i += 1
        # cv2.imshow("img_{}".format(i), mask)
    return new_points


def draw_circles(my_points):
    for my_point in my_points:
        cv2.circle(frame_copy, (my_point[0], my_point[1]), 10, my_color_values[my_point[2]], cv2.FILLED)


def find_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            cv2.drawContours(frame_copy, contour, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y


while True:
    success, frame = cap.read()
    if not success:
        print("Over")
        break
    frame_copy = frame.copy()
    new_points = find_color(frame)

    if len(new_points) != 0:
        my_points += new_points

    if len(my_points) != 0:
        draw_circles(my_points)

    cv2.imshow("img", frame_copy)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
