import cv2
import numpy as np

img = cv2.imread("simulator_imgs/room_2.png")
h, w, *_ = img.shape

top_img = cv2.imread("simulator_imgs/roomtop_2.png")
th, tw, *_ = img.shape

def showImg(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)

def showImgs(img1, img2, img3):
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)
    cv2.waitKey(0)
 
pts1 = np.float32([
    [782, 522-25], [1138, 522-25], [0, h-119], [w, h-119]
])

pts2 = np.float32([
    [0, 0], [w, 0], [0, h], [w, h]
]) 

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (w, h))

for pt in pts1:
    x, y = pt
    cv2.circle(img, (x, y), 20, (0, 0, 255), 3)

cv2.imwrite('imgs/warp1.jpg', img)

showImg(img)

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

#showImgs(new_truth, new_perpe)
#showImg(img)
#showImg(top_img)

# Grab bottom of boxes?
# Transform base on y axis (another perspective warp)

# Reconstruct from perspective plane of the tops of the boxes

pts1 = np.float32([
    [782, 522], [1138, 522], [0, h-89], [w, h-89]
])

pts2 = np.float32([
    [0, 0], [w, 0], [0, h], [w, h]
]) 

M = cv2.getPerspectiveTransform(pts1, pts2)

dst3 = cv2.warpPerspective(img, M, (w, h))

newer_perpe = cv2.resize(img,  (w  // (261 // 56),  h), interpolation = cv2.INTER_AREA)

showImgs(new_truth, new_perpe, newer_perpe)

cv2.imwrite('imgs/warp3.jpg', img)
cv2.imwrite('imgs/warp4.jpg', new_perpe)
cv2.imwrite('imgs/warp5.jpg', new_truth)