import cv2
import random
img = cv2.imread('logo/apple.png', -1)

#print(img.shape) # The output of this command be like : --> [rows, cloumns, channels]--> [520, 860, 4] --> which represents the (blue, green, red) color
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 