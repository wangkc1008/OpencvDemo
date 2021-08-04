"""
Create Date: 2021/7/28
Create Time: 20:26
Author: wangkc
"""

import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)          # 高斯模糊
img_canny = cv2.Canny(img, 100, 100)                      # canny算子边缘检测
kernel = np.ones((5, 5), np.uint8)
img_dilate = cv2.dilate(img_canny, kernel, iterations=1)  # 膨胀
img_erode = cv2.erode(img_dilate, kernel, iterations=1)   # 腐蚀

cv2.imshow("gray img", img_gray)
cv2.imshow("blur img", img_blur)
cv2.imshow("canny img", img_canny)
cv2.imshow("dilate img", img_dilate)
cv2.imshow("erode img", img_erode)
cv2.waitKey(0)


