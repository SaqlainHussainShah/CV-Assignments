#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 06:28:52 2019

@author: saqlain
"""

## 
import cv2
import numpy as np

img1 = cv2.imread('Q3_4.tif')
img = cv2.medianBlur(img1,5)

cv2.destroyAllWindows()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    perimeter = cv2.arcLength(cnt,True)
    if perimeter>150:
#        cv2.drawContours(img, contours, -1, (255,255,255), 3)
        cv2.circle(img,(cX,cY), 37, (2,100,255), 4)
    if perimeter<150:
#        cv2.drawContours(img, contours, -1, (15,15,15), 3)
        cv2.circle(img,(cX,cY), 20, (255,0,255), 2)

#    print(area)
#    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #count number of arcs to make a contour 
#    print(len(approx))
#    print("area", area)
    
#    area = cv2.contourArea(cnt)
#
#    if area>4000:
#        img = cv2.drawContours(img, contours, -1, (255,255,255), 3)
#    if area<=4000:
#        img = cv2.drawContours(img, contours, -1, (100,55,23), 3)


#    if 4000>area:
#        if area>2000:
#            
#            img = cv2.drawContours(img, contours, -1, (0,0,0), 3)

#    if area<2000:
#        img=cv2.drawContours(img,contours,-1,(100,100,100), 3)
#img2.shape=img.shape
cv2.imshow("Original image blurred and Blobs separated ",np.hstack([img1,img]))
cv2.waitKey()
cv2.destroyAllWindows()