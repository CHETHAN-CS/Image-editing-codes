import cv2

import numpy as np

img = cv2.imread("rmbgtest.jpg")
cv2.imshow('Input Image', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('greyscale.jpg', gray_img)

cv2.imshow('greyscale.jpg', gray_img)

cv2.waitKey(0)