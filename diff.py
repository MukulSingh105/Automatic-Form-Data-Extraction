import cv2
import numpy as np

img1 = cv2.imread("0003.jpg")
img2 = cv2.imread("0002.jpg")
# print(cv2.shape, cv1.shape)
diff = cv2.absdiff(img1, img2)
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

th = 1
imask =  mask>th

canvas = np.zeros_like(img2, np.uint8)
canvas[imask] = img2[imask]

cv2.imwrite("result.png", canvas)
