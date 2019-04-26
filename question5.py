x#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 06:28:52 2019

@author: saqlain
"""

## Propose a method to identify and locate the objects of each category in the image
## so that they can be picked up by a robotic system and placed in different bins


import numpy as np
import cv2

img2 = cv2.imread('Task 5.png')
img=img2.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray scale

ret,thresh = cv2.threshold(gray,127,255,0) #randomly selected threshold

contours,h = cv2.findContours(thresh,1,2) # built in funcino to find contours

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #count number of arcs to make a contour 
#highlight different contours in different ways based on number of sides
    if len(approx)==4:
        print("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),3) #draw contours on image
    elif len(approx) == 9:
        print("half-circle")
        cv2.drawContours(img,[cnt],0,(255,255,0),3)
    elif (len(approx) > 9 ):
        print("circle")
        cv2.drawContours(img,[cnt],0,(10,100,100),3)
        if len(approx)>=14:
            print("Hole")
            cv2.drawContours(img,[cnt],0,(100,0,10),3)
        


cv2.imshow('image',np.hstack([img2,img])) #show image with contours highlighted differently
cv2.waitKey(0)
cv2.destroyAllWindows()