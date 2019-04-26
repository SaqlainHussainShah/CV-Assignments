#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:10:37 2019

@author: saqlain
Question 1 Detect objects in image
"""
#correlation

import cv2
import numpy as np


image=cv2.imread("car.png",cv2.IMREAD_GRAYSCALE)
kernel=cv2.imread("template.png",cv2.IMREAD_GRAYSCALE)

[rows,cols]=image.shape[:2]
[k_rows,k_cols]=kernel.shape[:2]
print("rows", rows,"cols", cols,"k rows", k_rows,"k cols", k_cols)
x=np.zeros((rows,cols), dtype="uint8")
img_tmp=np.zeros((k_rows,k_cols)) 

    
for i in range(rows-k_rows):
    for j in range(cols-k_cols):
        img_tmp=image[i:i+k_rows,j:j+k_cols]
        sub = img_tmp-kernel;
        sub=sum(sum(sub))
#        print(sub)
        if np.all(sub==00):
            print(sub)
            print('match found', i, j)
            cv2.rectangle(image,(j,i),(j+k_cols,i+k_rows),(255,255,255),3)
            
cv2.imshow("template found using subtraction", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
            
#            cv2.imshow('found',img_tmp)
#            cv2.waitKey()
#            cv2.destroyAllWindows()
        
#        sum=sum(sum(kernel.*image[i:i+k_rows,j:j+k_cols]))
#        x[i,j]=sum(sum(image[i:i+k_rows, j:j+k_cols]-kernel))
#        x[i,j]=np.dot(image[i:i+k_cols,j:j+k_cols], kernel)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
#        err = np.sum((kernel.astype("float") - image[i:i+k_rows,j:j+k_cols].astype("float")) ** 2)
#        sum=sum((sum(kernel*image[i:i+k_rows,j:j+k_cols]))

#g=np.
        
   


        
    


#
#image=image/255
#kernel=kernel/255
#for i in range(h, image_h-h):
#    for j in range(w,image_w-w):
#        sum=0
#        for m in range(kernel_h):
#            for n in range(kernel_w):
#               sum=sum+kernel[m][n]*image[i-h+m][j-w+n]
#               image_conv[i][j]=sum
#      
#cv2.imshow("Imagge conv", image_conv)  
#cv2.waitKey(0)
#cv2.destroyAllWindows()    
#maxElement = np.amax(image_conv[:])
#print(maxElement)
#locax=np.zeros((5,5), dtype='int')
#locay=np.zeros((5,5), dtype='int')
#g=0       
#s,t=image_conv.shape[::2]
#for s in range(s):
#    for t in range(t):
#        if image_conv[s][t].any(maxElement) :
#            locax[g]=s
#            locay[g]=t
#            g=g+1
#            
#print(g)
#row,col=image_conv.shape[::2]
#a=0
##for x in range(row):
##    for y in range(col):
##        if image_conv[x][y]>180:
##            a=a+1
###maxElement = np.amax(image_conv[:])
###print(maxElement)
###max=np.zeros((2,2))
##print(a)
#winner = np.argwhere(image_conv == np.amax(image_conv))
#print(winner)


#arg=np.zeros((3,3))
#
#for x in range(row):
#    for y in range(col):
       
        
                    
            


#def corr(image, kernel):
#    image_h=image.shape[0]
#    image_w=image.shape[1]
#    
#    kernel_h=kernel.shape[0]
#    kernel_w=kernel.shape[1]
#    
#    h=kernel_h//2
#    w=kernel_w//2
#    
#    image_conv=np.zeros(image.shape)
#    
#    for i in range(h, image_h-h):
#        for j in range(w, image_w-w):
#            sum=0
#            
#            for m in range(kernel_h):
#                for n in range(kernel_w):
#                    sum=sum+kernel[m][n]*image[i-h+m][j-w+n]
#            
#            image_conv[i][j]=sum
#    return image_conv

#img1=cv2.imread("cars.png")
#img2=cv2.imread("template.png")
#
#corelat=corr(img1,img2)
