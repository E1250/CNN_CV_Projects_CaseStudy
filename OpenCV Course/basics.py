import cv2 as cv
PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


img = cv.imread(PATH_IMG+"1.jpeg")
'''cv.imshow("Cat",img)'''


###* Conveting to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
'''cv.imshow("Gray",gray)'''

###* Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) # There are many alternative of GaussianBlur , But we will use this
'''cv.imshow("Blur",blur)'''

###* Edge Cascade
""" When we applying Blur Before this , we will get lower Edge Detection"""
canny = cv.Canny(img,125,175)  # There are many alternative of GaussianBlur , But we will use this
'''cv.imshow("Blur",canny)'''

###* Dilaing the Image
dilated = cv.dilate(canny,(3,3),iterations = 1)
'''cv.imshow("Blur",dilated)'''

###* Eroding
""" Back to cascade"""
eroded = cv.erode(dilated,(3,3,),iterations=3)
'''cv.imshow("Blur",eroded)'''

###* Resize
""" Ignoring Aspect Issue"""
resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
'''cv.imshow("Blur",resized)'''

###* Cropping
cropped = img[100:200,100:200]
'''cv.imshow("Blur",cropped)'''











cv.waitKey(0)