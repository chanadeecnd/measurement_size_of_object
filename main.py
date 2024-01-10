import cv2
import numpy as np
import utils
#####################
# if using a camera, set webcam to Ture.
webcam = False

path = "./image/"
filename = "4.jpg"

# Setting camera
if webcam:
    cap = cv2.VideoCapture(0)
    cap.set(10, 160)
    cap.set(3, 1920)
    cap.set(4, 1080)

while True:
    if webcam: success, img = cap.read()
    else: img = cv2.imread(path + filename)
    
    img = cv2.resize(img, (0,0), None, 0.5, 0.5)

    img, finalContours = utils.getContours(img,showCanny=True, draw=True)
    #setting width and height 50%
    cv2.imshow('Original', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
        