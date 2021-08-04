"""
Create Date: 2021/7/28
Create Time: 21:00
Author: wangkc
"""
import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)  # 高 宽 通道 hwc

img_resize = cv2.resize(img, (300, 200))  # 宽 高
print(img_resize.shape)  # 高 宽 通道

img_crop = img[0:200, 200:500]  # 先裁y轴，再裁x轴

cv2.imshow("img", img)
# cv2.imshow("resize img", img_resize)
cv2.imshow("crop img", img_crop)
cv2.waitKey(0)