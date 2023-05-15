import cv2

#Opencv DNN 
net = cv2.dnn.readNet()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)
    cv2.waitkey(1)
