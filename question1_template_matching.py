#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:15:41 2019

@author: saqlain
"""
## question 1 object detection using template matching
import cv2
import numpy as np

img=cv2.imread("car.png")
img_bgr=img.copy()
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY) #convert to grayscale

template=cv2.imread("template.png",0)
w,h=template.shape[::-1]

res=cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED) #find correlation between images
threshold=0.44
loc=np.where(res>=threshold) #find where similarity is more than 0.42

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2) #draw rectangle where res>=threshold

cv2.imshow('Input image and template matched image', np.hstack([img, img_bgr])) #show image with highlighted matched points
cv2.waitKey(0) #wait for key press
cv2.destroyAllWindows() #close all windows