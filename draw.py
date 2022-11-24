import cv2 as cv
from cv2 import FILLED
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

'''
#1.Paint image on certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)
'''
#2. Draw rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), FILLED)
#cv.imshow('Rectangle', blank)

#3. Draw circle
cv.circle(blank, (250,250),50,(0,0,255),2)
#cv.imshow('Circle', blank)

#4. Draw line
cv.line(blank, (0,0), (250,250), (255,255,255), 2)
#cv.imshow('Line', blank)

#5. Text
cv.putText(blank, 'Test', (350,50), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)