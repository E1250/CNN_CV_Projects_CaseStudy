import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Line",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked = cv.bitwise_and(img,img,mask = mask)


#* GrayScale Histogram
# Drawing Distripution of Pixels
# gray_hist = cv.calcHist([gray],[0],mask , [256],[0,256])
'''
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

'''

#* Color Histogram
colors = ('b','g','r')
plt.figure() 
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()







cv.waitKey(0)