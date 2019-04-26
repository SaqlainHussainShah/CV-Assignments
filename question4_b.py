#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:03:36 2019

@author: saqlain
"""
#Q4
## b select two ROI and do histogram matching of first w.r.t second

import numpy as np
import cv2

#include functions in other files histogram.py and cumulative_histogram.py
import histogram as h
import cumulative_histogram as ch









 
    # Read image
im = cv2.imread("lena.png",0)
     
    # Select ROI
r = cv2.selectROI(im)
 
# Crop image
img = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# select second ROI
r2 = cv2.selectROI(im)
 
# Crop image
img_ref = im[int(r2[1]):int(r2[1]+r[3]), int(r2[0]):int(r2[0]+r2[2])]
 

cv2.imshow("first ROI original", img)

height = img.shape[0]
width = img.shape[1]
pixels = width * height #total pixels in first ROI

height_ref = img_ref.shape[0]
width_ref = img_ref.shape[1]
pixels_ref = width_ref * height_ref #total pixels in second ROI

#calculate histograms of both ROI
hist = h.histogram(img)
hist_ref = h.histogram(img_ref)

#Calculate cumulative histograms of both ROI
cum_hist = ch.cumulative_histogram(hist)
cum_hist_ref = ch.cumulative_histogram(hist_ref)

#Normalize cumulative histograms
prob_cum_hist = cum_hist / pixels
prob_cum_hist_ref = cum_hist_ref / pixels_ref

K = 256
new_values = np.zeros((K))

#histogram specification
for a in np.arange(K):
    j = K - 1
    while True:
        new_values[a] = j
        j = j - 1
        if j < 0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
            break
for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = new_values[a]
        img.itemset((i,j), b)

cv2.imshow('first ROI after histogram matching/specification', img)

  
cv2.waitKey(0) #wait for key press
cv2.destroyAllWindows() #close all windows