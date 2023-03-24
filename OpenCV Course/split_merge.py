import cv2 as cv
import numpy as np

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


img = cv.imread(PATH_IMG+"1.jpeg")
# cv.imshow("Line",img)
blank = np.zeros(img.shape[:2],dtype='uint8')

#* Spliting the image to Blue,Green,Red
b,g,r = cv.split(img)

# cv.imshow("Blue",b)
# cv.imshow("Gree",g)
# cv.imshow("Red",r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Gree",green)
cv.imshow("Red",red)



print(f"Image Shape: {img.shape},\n Blue Shape: {b.shape},\n Green Shape: {g.shape},\n Red Shape: {r.shape}")

#* Merging these image channels together
merged = cv.merge([b,g,r])
cv.imshow("Merged",merged)


cv.waitKey(0)