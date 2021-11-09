import cv2
import numpy as np
import cv2.aruco as aruco
import os

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters_create()

vid = cv2.VideoCapture(0)
while True:
    ret, img = vid.read()
    (corners, ids, rejects) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
    print(img.shape)
    cv2.aruco.drawDetectedMarkers(image=img, corners=corners, ids=ids)
    cv2.imshow("detection", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()