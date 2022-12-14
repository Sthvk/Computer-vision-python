import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
#features = np.load('features.npy', allow_pickle=True)
#labels = np.load('labels.npy')

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.read('face_trained.yml')

img = cv.imread('Resources\Faces\\val\\madonna\\5.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recogniser.predict(faces_roi)
    print(f'Detected {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (30,30), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('Detected Face', img)

cv.waitKey(0)