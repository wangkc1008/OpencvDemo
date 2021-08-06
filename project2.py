"""
Create Date: 2021/8/5
Create Time: 19:46
Author: wangkc
"""
import cv2
import numpy as np
from ImageStack import stackImages

frame_width = 480
frame_height = 640

# cap = cv2.VideoCapture("Resources/paper.jpg")
# cap.set(3, frame_width)
# cap.set(4, frame_height)
# cap.set(10, 150)


def preprocess(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_blur = cv2.GaussianBlur(frame_gray, (5, 5), 1)
    frame_canny = cv2.Canny(frame_blur, 200, 200)
    kernel = np.ones((5, 5))
    frame_dilate = cv2.dilate(frame_canny, kernel, iterations=2)
    frame_erode = cv2.erode(frame_dilate, kernel, iterations=1)

    return frame_erode


def get_contours(frame):
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    max_area = 0
    biggest_approx = np.array([])
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(frame_copy, contour, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                max_area = area
                biggest_approx = approx

    return biggest_approx


def reorder_points(biggest_approx):
    my_points = biggest_approx.reshape((biggest_approx.shape[0], biggest_approx.shape[-1]))
    print(my_points)
    my_new_points = np.zeros(biggest_approx.shape, dtype=np.int32)

    diff = np.diff(my_points, axis=1)
    my_new_points[0] = my_points[np.argmin(my_points.sum(axis=1))]
    my_new_points[1] = my_points[np.argmin(diff)]
    my_new_points[2] = my_points[np.argmax(diff)]
    my_new_points[3] = my_points[np.argmax(my_points.sum(axis=1))]

    return my_new_points


def warp_img(img, my_new_points):
    pst1 = np.array(my_new_points, np.float32)
    pst2 = np.array([[0, 0], [frame_width, 0], [0, frame_height], [frame_width, frame_height]], np.float32)
    matrix = cv2.getPerspectiveTransform(pst1, pst2)  # 获得投射变换后的矩阵
    img_o = cv2.warpPerspective(img, matrix, (frame_width, frame_height))  # 根据投射变换矩阵获得变换后的图像
    img_o_crop = img_o[20:img_o.shape[0] - 20, 20:img_o.shape[1] - 20]
    img_o_crop = cv2.resize(img_o_crop, (frame_width, frame_height))
    return img_o_crop


# while True:
#     success, frame = cap.read()
#     if not success:
#         print("Over")
#         break
frame = cv2.imread("Resources/paper.jpg")
frame = cv2.resize(frame, (frame_width, frame_height))
frame_copy = frame.copy()
frame_res = preprocess(frame)
biggest_approx = get_contours(frame_res)
print(biggest_approx)
my_new_points = reorder_points(biggest_approx)
print(my_new_points)
img_res = warp_img(frame, my_new_points)
cv2.imshow("img", img_res)
cv2.waitKey(0)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
