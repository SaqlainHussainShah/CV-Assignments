#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:36:48 2019

@author: saqlain
"""

# Question 3
## a. Remove noise from image Q3_1

#import libraries
import numpy as np
import cv2


#For removing noise one way is to take many number of images and then take average
#but we donot have any source image or other images so another way is to 
## 1- find edges if we have effect of blurring that could be removed and edges are found
## 2- Edges are added to original image
## 3- Then remove salt and pepper noise for that we need to do smoothing

#read image
img=cv2.imread('Q3_1.tif', cv2.IMREAD_GRAYSCALE)

#get rows and colums for image
img=cv2.resize(img,(310,310)) #to fit in the screen of laptop
[rows, cols]=img.shape[:2] 

# 1------ Finding Edges------
blur_img_33=cv2.blur(img,(11,11)) #aneraging

img_edges=np.zeros([rows,cols], dtype="uint8") # store edges
image_enhanced_edges=np.zeros([rows,cols], dtype="uint8") #store image found by adding edges to original

img_edges=img-blur_img_33

# 2-------- Add edges to original ----
image_enhanced_edges=img+img_edges
orig_vs_enhanced_edges=np.hstack([img, img_edges, image_enhanced_edges]) #show improved edges and original image

# 3 -------Removing salt and pepper noise by smoothing ------
avg=cv2.blur(image_enhanced_edges,(11,11)) #Averaging for smoothing
gaus = cv2.GaussianBlur(image_enhanced_edges,(11,11),0) #Gaussian smoothing
med = cv2.medianBlur(image_enhanced_edges,11) # median blurring for removing salt and pepper noise

avg_gaus_med=np.hstack([avg, gaus,med]) #stack different averaged images in one variable for showing

#show images in sequence as per title
cv2.imshow('original, img edges,  enhanced edges, average, gaussian and median', np.vstack([orig_vs_enhanced_edges, avg_gaus_med] ))


cv2.waitKey(0) #wait until any key press
cv2.destroyAllWindows() # close all windows