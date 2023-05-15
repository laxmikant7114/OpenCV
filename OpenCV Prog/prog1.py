import cv2
img = cv2.imread('logo/phoenix.png', -1)
img = cv2.resize(img, (0, 0), fx=2, fy=2)
img = cv2.rotate(img, cv2.ROTATE_180) #It rotates the image to 90 Degree clockwise

cv2.imwrite('new_img.jpg', img)  #It creates new variable and stores the new Img in that
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
