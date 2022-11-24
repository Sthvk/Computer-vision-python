import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#mask = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
mask_shape = cv.rectangle(blank.copy(), (img.shape[1]//2 -50, img.shape[0]//2 - 50), (img.shape[1]//2 + 100, img.shape[0]//2 + 50), 255, -1)
cv.imshow('Mask', mask_shape)

mask = cv.bitwise_and(img, img, mask=mask_shape)
cv.imshow('Masked image', mask)

cv.waitKey(0)