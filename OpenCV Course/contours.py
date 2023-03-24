import cv2 as cv
import numpy as np


PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

img = cv.imread(PATH_IMG+"1.jpeg")

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny =cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)

# ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow("Thresh",thresh)

contours , hierarchies =  cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print("Contours: "+str(len(contours)))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Contours Drawed", blank)


cv.waitKey(0)