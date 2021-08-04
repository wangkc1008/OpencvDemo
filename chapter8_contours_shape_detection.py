"""
Create Date: 2021/7/30
Create Time: 19:52
Author: wangkc
"""
import cv2
import numpy as np

from ImageStack import stackImages


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        # print(contour)
        area = cv2.contourArea(contour)
        print(area)
        cv2.drawContours(img_copy, contour, -1, (255, 0, 0), 3)  # -1表示绘制所有的边界 颜色和粗细
        peri = cv2.arcLength(contour, True)  # True表示闭合曲线
        print(peri)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)  # 0.02 * peri表示最大的误差 True表示闭合曲线 返回所有的角的坐标
        print(len(approx))  # 表示有多少角
        x, y, w, h = cv2.boundingRect(approx)  # 计算边界矩形框
        num_cor = len(approx)

        if num_cor == 3:
            obj_type = "Triangle"
        elif num_cor == 4:
            if 0.95 < w / h < 1.05:
                obj_type = "Square"
            else:
                obj_type = "Rectangle"
        elif num_cor > 4:
            obj_type = "Circle"
        else:
            obj_type = "None"

        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 0), 3)
        cv2.putText(img_copy, obj_type, (x + w//2 - 10, y + h // 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 0, 0), 2)


path = "Resources/shapes.png"
img = cv2.imread(path)

img_copy = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)

print(img.shape)
img_blank = np.zeros_like(img)
print(img_blank.shape)

get_contours(img_canny)

img_s = stackImages(0.6, ([img, img_gray, img_blur], [img_canny, img_copy, img_blank]))
cv2.imshow("img_stack", img_s)
cv2.waitKey(0)