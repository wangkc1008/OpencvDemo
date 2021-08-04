"""
Create Date: 2021/7/30
Create Time: 18:13
Author: wangkc
"""
import cv2
import numpy as np

img = np.zeros([768, 512, 3], np.uint8)  # h w c
print(img.shape)

img[:] = 0, 255, 255

# cv2.line(img, (0, 0), (300, 300), (255, 0, 0), 10)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 10)  # 点的坐标（x， y）
cv2.rectangle(img, (0, 0), (250, 500), (0, 128, 0), cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 10)
cv2.putText(img, "哈哈", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 100), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
