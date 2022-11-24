import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/PXL_20220715_110200564.jpg')
#cv.imshow("Original", img)

resized_img = rescaleFrame(img, 0.2)
cv.imshow('Image', resized_img)

gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)