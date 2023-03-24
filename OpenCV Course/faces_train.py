import os
import numpy as np
import cv2 as cv

people = [] # Names
DIR = r''
haar_casecade = cv.CascadeClassifier('cv_course\haar_face.xml')

# p = []
# for i in os.listdir(r''): # Add here folder of your pics
#     p.append(i)   
# print(p)

features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_casecade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
            
            for (x,y,w,h) in faces_rect :   
                faces_roi = gray[ y:y+h , x: x+w]
                features.append(faces_roi)
                labels.append(label)
            
            
create_train()
print("---------------------- Training Done --------------------------------------")
print(f'Length of the features = {len(features)}')        
print(f'Length of the lables = {len(labels)}')        

features = np.array(features,dtype='object')
labels = np.array(labels)

face_recogniser = cv.face.LBPHFaceRecognizer_create()

# Train the recogniser of the features list and the labels list
face_recogniser.train(features,labels)

face_recogniser.save('face _trained.yml')
np.save('features.npy' , features)
np.save('labels.npy' , labels)




