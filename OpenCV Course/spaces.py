import cv2 as cv
import matplotlib.pyplot as plt

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

img = cv.imread(PATH_IMG+"1.jpeg")
# cv.imshow("Main",img)
# plt.imshow(img)
# plt.show()

# BGR To Gray Scale
gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

# BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("LAB",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("LAB",lab)
# plt.imshow(rgb)
# plt.show()

#* you can not convert from `Grayscale` to `HSV`, you should: `Grayscale` => `BGR` => `HSV`
# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV => BGR",hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("LAB => BGR",lab_bgr)

cv.waitKey(0)