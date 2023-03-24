import cv2 as cv
import numpy as np

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow("Blank",blank)

###* print the image a certain colour * 
'''
blank[:] = 0,255,0 # change the range here `[200:300,300:400]` to draw inside
cv.imshow('Greed',blank)

'''
###* Draw a Outline Rectangel*

'''
cv.rectangle(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2),(0,255,0),thickness = 2) # you also can use `thickness = cv.FILLED` or `-1`
cv.imshow('Rectangle',blank)
'''

###* Drawing a Circle *
'''
cv.circle(blank,(blank.shape[1]//2 , blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow("Cricle",blank)
'''

###* Drawing a Line *
'''
cv.line(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2),(0,0,255),thickness=3)
cv.imshow("Line",blank)
'''

###* Write text in image*
'''
cv.putText(blank,"Hello",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("Text",blank)
'''

cv.waitKey(0)













