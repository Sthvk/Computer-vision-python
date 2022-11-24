import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)

'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
'''
mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)

#Color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

#(tuple with elements - b, g, r)
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)