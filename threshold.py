import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple threshold
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold', thresh_inv)

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresh', adaptive_threshold)

cv.waitKey(0)