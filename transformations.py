import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

''''''

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> left; -y -> up
# +x -> right; +y -> down

translated = translate(img, 100, 100)
#cv.imshow('Translated', translated)

''''''

# Rotation
def rotate(img, angle, roatationPoint=None):
    (height, width) = img.shape[:2]

    if roatationPoint is None:
        roatationPoint = (width//2, height//2)

        rotMat = cv.getRotationMatrix2D(roatationPoint, angle, scale = 1.0)
        dimensions = (width, height)

        return cv.warpAffine(img, rotMat, dimensions)
    
rotated = rotate(img, -45)
#cv.imshow('Rotated', rotated)

''''''

# Flip
# 0 - vertical flip; 1 - horizontal flip; -1 both
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

cv.waitKey(0)