import cv2 as cv
import numpy as np
PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Line",img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank Image",blank)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("Mask",mask)

masked = cv.bitwise_and(img,img,mask = mask)
cv.imshow("Masked",masked)

cv.waitKey(0)