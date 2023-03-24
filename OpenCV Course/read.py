import cv2 as cv

PATH_IMG = "C:/Users/lenovo/Desktop/VSCode/cv_course/images/"
PATH_VID = "C:/Users/lenovo/Desktop/VSCode/cv_course/videos/"

###*************************************Functions*******************************###
###*Resizing and Scaling*
def rescaleFrame(frame,scale=0.75):
    """
    Used in Images , Videos and Live Videos
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


###*Changing Resolution*
def changeRes(width,height):
    """
    Works only with Live Video (webcams)
    """
    capture.set(3,width)  # 3 Represents the Width
    capture.set(4,height)  # 4 Represents the height
    # capture.set(10,height)  # 10 Represents the Brightness
###***************************Functions***************************###

###* Showing Images and Videos*#
# *Showing Images*
'''
img = cv.imread(PATH_IMG+"1.jpeg")
cv.imshow("Cat",img)
cv.waitKey(0)

'''

# *Reading Videos*

capture = cv.VideoCapture(PATH_VID+"1.mp4") # Use 0 if you are using webcam
while True:
    isTrue , frame = capture.read() # Returns by Frame
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()





