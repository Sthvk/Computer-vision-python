import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Original", img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#gaussian blur - to reduce unnecessory noise
#increse kernel value (2nd parameter - odd nos only) for higher blur
blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur,125,175)
cv.imshow('Canny', canny)

#Dilation
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)
'''
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow('Dilated', dilated)
'''

#Erosion
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

#crop
croppped = img[50:200,200:400]
cv.imshow('Cropped', croppped)


cv.waitKey(0)
