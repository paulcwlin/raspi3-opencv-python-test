# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:11:47 2021

@author: d19fd
"""

import cv2

img = cv2.imread('lena.bmp', 0)
cv2.imshow('before', img)
for i in range(10, 100):
    for j in range(80, 100):
        img[i,j]=255
cv2.imshow('after', img)
cv2.waitKey()
cv2.destroyAllWindows()