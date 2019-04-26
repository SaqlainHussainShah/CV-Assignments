#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:51:29 2019

@author: saqlain
"""
#Question 3
##   b. Extract the gradient parts from the input image Q3_2.
# To find gradient parts I have used three different filters
## 1- Laplacian
## 2- Sobel
## 3- Canny

#Import useful libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

#read image
img = cv2.imread('Q3_2.tif',0)

# 1- Laplacian is a 2-D isotropic measure of the 2nd spatial derivative of an image. 
#    The Laplacian of an image highlights regions of rapid intensity change
#    Laplacian is often used for edge detection
laplacian = cv2.Laplacian(img,cv2.CV_64F)

#The Sobel operator performs a 2-D spatial gradient measurement on an image
# It emphasizes regions of high spatial frequency that correspond to edges.
# It is used to find the approximate absolute gradient magnitude at each point in an input grayscale image
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


# The Canny edge detector is an edge detection operator
## Canny uses a multi-stage algorithm to detect a wide range of edges in images
canny_edge = cv2.Canny(img,100,200)

#Show original image and gradient found using laplacian and sobel
#plt.subplot(2,2,1)
#plt.imshow(img,cmap = 'gray')
cv2.imshow("original Image ", img)
#plt.title('Original')
#plt.subplot(2,2,2)
#plt.imshow(laplacian,cmap = 'gray')
cv2.imshow("Gradient found using Laplacian", laplacian)
#plt.title('Laplacian')
#plt.subplot(2,2,3)
#plt.imshow(sobelx,cmap = 'gray')
cv2.imshow("Gradient found using Sobel along x axis",sobelx)
#plt.title('Sobel X')
#plt.subplot(2,2,4)
#plt.imshow(sobely,cmap = 'gray')
cv2.imshow('Gradient found using sobel along y axis', sobely)
#plt.title('Sobel Y')
#plt.show()
cv2.imshow("Gradient found using canny edge detector", canny_edge)
cv2.waitKey(0) # wait until key press
cv2.destroyAllWindows() #close all windows