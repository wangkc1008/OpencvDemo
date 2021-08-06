"""
Create Date: 2021/8/5
Create Time: 21:48
Author: wangkc
"""
import cv2
import numpy as np
import os

image_dir = "Resources/cars"
image_files = os.listdir(image_dir)
print(image_files)
image_files = [os.path.join(image_dir, image_file) for image_file in image_files]

car_plate_cascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

i = 0
while True:
    idx = np.random.randint(0, 3, 1, np.int32)[0]
    img = cv2.imread(image_files[int(idx)])

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    car_plates = car_plate_cascade.detectMultiScale(img_gray, 1.1, 4)
    for (x, y, w, h) in car_plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        cv2.putText(img, "plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
        area = w * h
        car_plate_img = np.zeros((h, w))
        if area > 500:
            car_plate_img = img[y:y+h, x:x+w]
            cv2.imshow("car_plate", car_plate_img)

    cv2.imshow("Result", img)
    cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/cars/scanned/car_plate_{}.jpg".format(i), car_plate_img)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan saved", (150, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)

    i += 1


