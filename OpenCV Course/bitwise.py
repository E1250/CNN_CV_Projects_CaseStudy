import cv2 as cv
import numpy as np

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv.imshow("Recotangle",rectangle)


circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("Circle",circle)

#* Bitwise AND 
"""Returns Intersection """
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise AND",bitwise_and)

#* Bitwise OR 
"""Returns Union """
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise OR",bitwise_or)

#* Bitwise XOR 
"""Returns NON Intersecting Region"""
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise XOR",bitwise_xor)

#* Bitwise XOR
"""Returns NON Intersecting Region"""
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise OR",bitwise_xor)

#* Bitwise NOT
"""Returns NON Intersecting Region"""
bitwise_not = cv.bitwise_not(rectangle,circle)
cv.imshow("Bitwise NOT",bitwise_not)



img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Line",img)



cv.waitKey(0)