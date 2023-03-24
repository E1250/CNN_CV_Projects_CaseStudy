import cv2 as cv
PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Line",img)

"""Thresholding is Binarization of an Image"""
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#! Simple Thresholding
threhold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)
cv.imshow("Simple Thresholded" , thresh)

threhold , thresh_inv = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded Inverse" , thresh_inv)

#! Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 3)
cv.imshow("Adaptive Thresholded" , adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV , 11 , 3)
cv.imshow("Adaptive Thresholded Inverse" , adaptive_thresh_inv)

cv.waitKey(0)