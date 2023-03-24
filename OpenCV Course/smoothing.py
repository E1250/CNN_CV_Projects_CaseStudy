import cv2 as cv
PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Line",img)

"""Here we are usign a window, like Filtering in Neural Network"""
#* Averiging
average = cv.blur(img,(7,7))   # high window, high Blur
cv.imshow("Average Blur",average)


#* Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian Blur",gauss)


#* Median Blur
median = cv.medianBlur(img,7)
cv.imshow("Median Blur",median)


#* Bilateral (Most Effective)
binlateral = cv.bilateralFilter(img,10,15,15)
cv.imshow("Binlateral Filter",binlateral)


cv.waitKey(0),