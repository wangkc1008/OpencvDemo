"""
Create Date: 2021/8/4
Create Time: 16:58
Author: wangkc
"""
import cv2
import numpy
from ImageStack import stackImages

face_cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# img = cv2.imread("Resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#
# img_s = stackImages(0.6, [img])
# cv2.imshow("img_stack", img_s)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        print("failed")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("face detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
