"""
Create Date: 2021/7/28
Create Time: 20:26
Author: wangkc
"""

import cv2

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources/test_video.mp4")
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(10, 100)  # 亮度

while True:
    success, frame = cap.read()
    if not success:
        break
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



