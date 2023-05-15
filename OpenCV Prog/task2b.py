import cv2 as cv
import numpy as np
#reading the image
img = cv.imread('yellow_detect.jpeg')
#converting image into HSV format
hsv_img = cv.cvtColor(img,cv.COLOR_RGB2HSV)
# cv.imshow('hsv_img',hsv_img)
#Applying Threshold
_,thresh = cv.threshold(hsv_img, 137,175,cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)  
#Applying GrayScale
grays = cv.cvtColor(thresh, cv.COLOR_BGR2GRAY)
#Applying Blur
blur= cv.GaussianBlur(grays,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur) 
#Applying Edge Detection
canny = cv.Canny(blur, 125,175)
# M = cv.moments(canny)
# cX = int(M["m10"] / M["m00"])
# cY = int(M["m01"] / M["m00"])
contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# contours1 = contours[1]
# contours2 = contours[0]

# blank1= np.zeros(img.shape, dtype='uint8')
# blank2= np.zeros(img.shape, dtype='uint8')

# cv.drawContours(blank1,contours1,-1,(255,255,255),1)
# cv.drawContours(blank2,contours2,-1,(255,255,255),1)
# cv.imshow('cont1',blank1)
# cv.imshow('cont2',blank2) 
M = cv.moments(contours[0])

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(cx , cy)
# print(cx1 , cy1)
# print(f'{len(contours)}contours')
# cv.imshow('canny',canny)
# cv.waitKey(0)
# cv.destroyAllWindows()

 
 

