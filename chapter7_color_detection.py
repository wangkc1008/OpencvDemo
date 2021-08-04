"""
Create Date: 2021/7/30
Create Time: 19:21
Author: wangkc
"""
import cv2
import numpy as np
from ImageStack import stackImages


def empty(a):
    pass


path = "Resources/lambo.png"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 32, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 71, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # HSV颜色模型 色调 饱和度 明亮度
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    img_o = cv2.bitwise_and(img, img, mask=mask)

    img_s = stackImages(0.6, ([img, img_hsv], [mask, img_o]))
    cv2.imshow("img_stack", img_s)
    # cv2.imshow("img", img)
    # cv2.imshow("img_hsv", img_hsv)
    # cv2.imshow("mask", mask)
    # cv2.imshow("img_o", img_o)
    cv2.waitKey(1)
