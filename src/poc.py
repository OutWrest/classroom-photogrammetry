import cv2
import numpy as np

img = cv2.imread("simulator_imgs/room_1.png")
h, w, *_ = img.shape

top_img = cv2.imread("simulator_imgs/roomtop_1.png")
th, tw, *_ = img.shape

def showImg(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
 
pts1 = np.float32([
    [782, 522], [1138, 522], [0, h], [w, h]
])

pts2 = np.float32([
    [0, 0], [w, 0], [0, h], [w, h]
]) 

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (w, h))

for pt in pts1:
    x, y = pt
    cv2.circle(img, (x, y), 20, (0, 0, 255), 3)

#showImg(img)
#showImg()
#showImg(dst)

pts1 = np.float32([
    [795, 62], [1125, 62], [795, 767], [1125, 767]
])

pts2 = np.float32([
    [0, 0], [w, 0], [0, h], [w, h]
]) 

M = cv2.getPerspectiveTransform(pts1, pts2)

dst2 = cv2.warpPerspective(top_img, M, (w, h))

for pt in pts1:
    x, y = pt
    cv2.circle(top_img, (x, y), 20, (0, 0, 255), 3)

# 261, 56;

new_truth = cv2.resize(dst2, (tw // (261 // 56), th), interpolation = cv2.INTER_AREA)
new_perpe = cv2.resize(dst,  (w  // (261 // 56),  h), interpolation = cv2.INTER_AREA)

showImg(new_truth)
showImg(new_perpe)