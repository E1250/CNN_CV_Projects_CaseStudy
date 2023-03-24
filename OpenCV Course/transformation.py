import cv2 as cv
import numpy as np

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"


img = cv.imread(PATH_IMG+"1.jpeg")

###* Trainslation
"""Shifting an image in `x` or `y` Axis"""
def translate(img,x,y):
    """
     -x --> Left
     -y --> Up
      x --> Right
      y --> Down
      
    """
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


translated = translate(img,50,50)
'''cv.imshow("Line",translated)'''

###* Rotatoin
def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
'''cv.imshow("Line",rotated)'''

###* Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
'''cv.imshow("Line",resized)'''

###* Flipping
"""Flipping Horizontly or Vertically"""
flip = cv.flip(img,-1) # 0,1,-1  try them
cv.imshow("Line",flip)



# cv.imshow("Line",rotated)
cv.waitKey(0)


