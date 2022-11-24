import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

#Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average blur', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

#Bilateral blur:
# Applies blur while keeping edges intact. 
# Slower than other methods
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral blur', bilateral)

cv.waitKey(0)