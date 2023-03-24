import cv2 as cv
PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


# img = cv.imread(PATH_IMG+"pic.jpg")
img = cv.imread(PATH_IMG+"people.jpg")
img = cv.resize(img , (500,500))

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person' , gray)


haar_casecade = cv.CascadeClassifier('cv_course\haar_face.xml')

faces_rect = haar_casecade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f"Number of faces found = {len(faces_rect)}")


for (x,y,w,h) in faces_rect :
    cv.rectangle(img,(x,y) , (x+w , y+h) , (0,255,0) , thickness = 2)
    
cv.imshow('Detected Faces' , img)



cv.waitKey(0)