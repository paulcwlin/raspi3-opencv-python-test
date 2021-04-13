import cv2
import numpy as np

img = cv2.imread('m2.jpg')
hist = cv2.calcHist([img], [0], None, [256], [0,255])

print(type(hist))
print(hist.shape)
print(hist.size)
print(hist)