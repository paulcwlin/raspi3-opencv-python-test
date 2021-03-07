# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:03:26 2021

@author: d19fd
"""

import cv2
import numpy as np

img = cv2.imread('yuko.jpg')
rows, cols, ch = img.shape

p1 = np.float32([[0,0], [cols-1, 0], [0,rows-1]])
p2 = np.float32([[0, rows*0.33], [cols*0.85, rows*0.25], [cols*0.15, rows*0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('result', dst)

cv2.waitKey()
cv2.destroyAllWindows()
