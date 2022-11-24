import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Original',img)

#This would show inverted colors
#plt.imshow(img)
#plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

'''
#BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR TO L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)
'''

#BGR to HSV and reverse
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

hsv2bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -> BGR', hsv2bgr)

cv.waitKey(0)