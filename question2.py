#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:31:29 2019

@author: saqlain
"""

#Filter images using Gaussian and Median filtering
#Find the standard deviation which gives the minimum mean squared error 


import cv2
import numpy as np

# for image noisy1.png

img = cv2.imread('noisy1.png')
orig=cv2.imread('lena.png')
row, col= img.shape[:2]
print(row,col)
bottom= img[row-2:row, 0:col]


m_s_e=np.zeros((17), dtype='int') # store temporarily values to calculate mean square values
#print(m_s_e)
i=3 # for odd kernel size
mini=1000 # randomly selected for minimum mean square error value
min_deviation=0
#calculate minimum mean square error for different values of standard deviation
while i<=15:
    bordersize=i//2
    border=cv2.copyMakeBorder(img, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
    gaussianImg = cv2.GaussianBlur(img, ksize=(5,5), sigmaX=i)   
    m_s_e[i] = np.sum((gaussianImg.astype("float") - orig.astype("float")) ** 2)
    m_s_e[i] = m_s_e[i]/(row * col)
    if (m_s_e[i] <mini):
        mini=m_s_e[i]
        min_deviation=i
    i=i+2
    
print( "minimum minimum square error", mini, "minimum standard deviation", min_deviation)

#Now we can use deviation which causes minimum mean square error i-e min_deviation as calculated
min_gaussian_filter=cv2.GaussianBlur(img,ksize=(5,5), sigmaX=min_deviation)
cv2.imshow("Minimum deviation gaussian filtered", min_gaussian_filter)
    


cv2.imshow('input image',img)
print(gaussianImg.shape[:2])



# End of gaussian

# Median filter
i=3
minim=1000
min_mse_kernel=0
while i<=15:
    medianImg = cv2.medianBlur(img,i)
    m_s_e[i] = np.sum((medianImg.astype("float") - orig.astype("float")) ** 2)
    m_s_e[i] = m_s_e[i]/(row * col)
    if (m_s_e[i] <minim):
        minim=m_s_e[i]
        min_mse_kernel=i
    i=i+2

print("Minimum MSE ", minim, "minimum mse kernel" , min_mse_kernel)
min_median_filter=cv2.medianBlur(img, min_mse_kernel)
cv2.imshow("Minimum deviation median filtered", min_median_filter)


cv2.waitKey(0)
cv2.destroyAllWindows()

# end of median
# end of noisy1.png image

#for image noisy2.png

img = cv2.imread('noisy2.png') # read image noisy2.png
row, col= img.shape[:2]
bottom= img[row-2:row, 0:col]

m_s_e=np.zeros((17), dtype='int')

i=3
mini=1000
min_deviation=0
# calculate minimum mean square error standard deviation
while i<=15:
    bordersize=i//2
    border=cv2.copyMakeBorder(img, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
    gaussianImg = cv2.GaussianBlur(img, ksize=(i, i), sigmaX=i)
    
    m_s_e[i] = np.sum((gaussianImg.astype("float") - orig.astype("float")) ** 2)
    m_s_e[i] = m_s_e[i]/(row * col)
    if (m_s_e[i] <mini):
        mini=m_s_e[i]
        min_deviation=i
    i=i+2
    
print( "minimum mean square error.", mini, "Stndard deviation corresponding to minimum MSE", min_deviation)

#Now we can use deviation which causes minimum mean square error i-e min_deviation as calculated
min_gaussian_filter=cv2.GaussianBlur(img,ksize=(5,5), sigmaX=min_deviation)
cv2.imshow("Minimum deviation gausian filtered", min_gaussian_filter)
    


cv2.imshow('input image ',img)




# End of gaussian

# Median filter
i=3
minim=1000
min_mse_kernel=0
while i<=15:
    medianImg = cv2.medianBlur(img,i)
    m_s_e[i] = np.sum((medianImg.astype("float") - orig.astype("float")) ** 2)
    m_s_e[i] = m_s_e[i]/(row * col)
    if (m_s_e[i] <minim):
        minim=m_s_e[i]
        min_mse_kernel=i
    i=i+2

print( "minimum mse kernel" , min_mse_kernel)
min_median_filter=cv2.medianBlur(img, min_mse_kernel)
cv2.imshow("Minimum deviation median filtered", min_median_filter)


cv2.waitKey(0)
cv2.destroyAllWindows()

#End of noisy2