from typing import List
import cv2
import numpy as np

# Implements perspective warp functions

def warpTo(pts: List[List[float]], img: np.ndarray, resize_factor: float) -> np.ndarray:
    # Returns a warped image to the four corners of that image's h/w

    h, w, *_ = img.shape

    M = cv2.getPerspectiveTransform(
        np.float32(pts),
        np.float32([
        [0, 0], [w, 0], [0, h], [w, h]
        ])
    )

    warped = cv2.warpPerspective(img, M, (w, h))

    if resize_factor:
        return cv2.resize(warped,  (w  // resize_factor,  h), interpolation = cv2.INTER_AREA)

    return warped

