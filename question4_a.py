#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:05:57 2019

@author: saqlain
"""

# Q 4
## a. Region based Histogram Equalization

#import libraries
import cv2
import numpy as np

 
# Read image
im = cv2.imread("lena.png",0) #read input image
 
# Select ROI
r = cv2.selectROI(im) #randomly select region of interest
 
# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

equ = cv2.equalizeHist(imCrop) #equalize histogram of selected region
 #

# Display cropped image
cv2.imshow("Region of interest", imCrop)
cv2.imshow("histogram equalized of ROI", equ)
cv2.waitKey(0) #wait until key press
cv2.destroyAllWindows() #close all windows