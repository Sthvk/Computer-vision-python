import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/_MG_5718 (2).jpg')
#cv.imshow('Sathvik', img)

resized_img = rescaleFrame(img)
cv.imshow('Image', resized_img)
cv.imshow('Sathvik', img)

gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#threshold turns bit to 1 if value higher than 125; 0 otherwise
ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', threshold)

# Contours can be detected either from canny edges or threshold
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#contours, hierarchies = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

# Drawing the contours found on a blank image
blank = np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)