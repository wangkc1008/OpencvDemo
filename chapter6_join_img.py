"""
Create Date: 2021/7/30
Create Time: 18:56
Author: wangkc
"""
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

hor = np.hstack((img, img))  # 水平堆叠
ver = np.vstack((img, img))  # 竖直堆叠

cv2.imshow("hor img", hor)
cv2.imshow("ver img", ver)
cv2.waitKey(0)
