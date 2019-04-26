#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 05:59:26 2019

@author: saqlain
"""
#Question 3
##   C Extract the rice objects from image

## By looking at image we can find that intensity level of rice is higher than background
##  SO we can threshold 
## I could manually select thresholding value and get good results but
## I have used otsu threshold because it can automatically detect threshold

import cv2
import numpy as np

img=cv2.imread("Q3_3.tif")

img=cv2.resize(img,(400,500))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #COnvert image to Grayscale
img2=img.copy()

(T, thresh_otsu) = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
( contours, _) = cv2.findContours(thresh_otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)
thresh_image=np.hstack([img,thresh_otsu, img2])
cv2.imshow("Thresholded Images",thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()