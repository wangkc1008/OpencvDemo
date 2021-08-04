"""
Create Date: 2021/7/30
Create Time: 18:44
Author: wangkc
"""
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
print(img.shape)  # hwc

width, height = 250, 350
pst1 = np.array([[111, 219], [287, 188], [154, 482], [352, 440]], np.float32)
pst2 = np.array([[0, 0], [width, 0], [0, height], [width, height]], np.float32)
cv2.line(img, [111, 219], [287, 188], (255, 0, 0), 2)
cv2.line(img, [111, 219], [154, 482], (255, 0, 0), 2)
cv2.line(img, [287, 188], [352, 440], (255, 0, 0), 2)
cv2.line(img, [154, 482], [352, 440], (255, 0, 0), 2)
matrix = cv2.getPerspectiveTransform(pst1, pst2)  # 获得投射变换后的矩阵
img_o = cv2.warpPerspective(img, matrix, (width, height))  # 根据投射变换矩阵获得变换后的图像

cv2.imshow("img", img)
cv2.imshow("img_o", img_o)
cv2.waitKey(0)