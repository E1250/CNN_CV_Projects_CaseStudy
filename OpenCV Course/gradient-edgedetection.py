import cv2 as cv
import numpy as np

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Line",img)


gray = cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
cv.imshow("Gray",gray)

#! Laplician
lap = cv.Laplacian(gray , cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#! Sobel
sobelx = cv.Sobel(gray , cv.CV_64F ,  1 , 0)
sobely = cv.Sobel(gray , cv.CV_64F ,  0 , 1)
combiend_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow("SobelX" , sobelx)
cv.imshow("SobelY" , sobely)
cv.imshow("Combined Sobel" , combiend_sobel)

#! Edge Detecting
canny = cv.Canny(gray , 150, 175)
cv.imshow("Canny" , canny)


cv.waitKey(0)