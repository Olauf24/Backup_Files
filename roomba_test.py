from __future__ import print_function
import time
from dual_mc33926_rpi import motors
from gpiozero import LED, PhaseEnableRobot
from time import sleep
from signal import pause
import cv2
import numpy as np
import cv2.aruco as aruco
import os

def forward():
    motors.motor1.setSpeed(300)
    motors.motor2.setSpeed(300)
    print("Go forward")
    
def backward():
    motors.motor1.setSpeed(-300)
    motors.motor2.setSpeed(-300)
    print("Go backward")
    
def forward_right():
    motors.motor1.setSpeed(300)
    motors.motor2.setSpeed(200)
    print("Go right")

def forward_left():
    motors.motor1.setSpeed(200)
    motors.motor2.setSpeed(300)
    print("Go left")
    
def stop():
    motors.setSpeeds(0, 0)
    print("Stop")
    
def run():
    motors.enable()
    print("Run")
    
def PLAY():
    ret, img = vid.read()
    (corners, ids, rejects) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
    cv2.aruco.drawDetectedMarkers(image=img, corners=corners, ids=ids)
    cv2.imshow("detection", img)
    
run()
while True:

    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
    arucoParams = cv2.aruco.DetectorParameters_create()

    vid = cv2.VideoCapture(0)
    if PLAY:
        forward_right()

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        
    vid.release()
    cv2.destroyAllWindows()

# forward_right()
# time.sleep(2)
# forward_left()
# time.sleep(2)
# stop()