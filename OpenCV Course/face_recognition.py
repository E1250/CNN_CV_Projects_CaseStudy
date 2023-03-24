import numpy as np
import cv2 as cv

haar_casecade = cv.CascadeClassifier('cv_course\haar_face.xml')

people = [] # Names
features = np.loas('features.npy',allow_pickle=True)
labels = np.load('labels.npy',allow_pickle=True)

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.read('face _trained.yml')

img = cv.imread(r'')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person' , gray)

# Detect the face in the image
faces_rect = haar_casecade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
for (x,y,w,h) in faces_rect:
    faces_foi = gray[y:y+h,x:x+h]
    
    label , confidence = face_recogniser.predict(faces_foi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img,str(people[label]) , (20,20) , cv.FONT_HERSHEY_COMPLEX , 1 , (0,255,0),thickness=2)
    cv.rectangle(img,(x,y) , (x+w , y+h) , (0,255,0) , thickness = 2)


cv.imshow('Detected Face' , img)
cv.waitKey(0)




