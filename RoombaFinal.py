from __future__ import print_function
import time
from dual_mc33926_rpi import motors
from gpiozero import PhaseEnableRobot
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
    motors.motor1.setSpeed(250)
    motors.motor2.setSpeed(175)
    print("Go right")

def forward_left():
    motors.motor1.setSpeed(175)
    motors.motor2.setSpeed(250)
    print("Go left")
    
def spin_left():
    motors.motor1.setSpeed(175)
    motors.motor2.setSpeed(-175)
    print("Spin left")  
    
def stop():
    motors.setSpeeds(0, 0)
    print("Stop")
    
def run():
    motors.enable()
    print("Run")

tc = 0

duty_cycles = list(range(0, 101)) + list(range(100, -1, -1))
i = 0
FLAG = False
run_time = 0

try:
    motors.enable()
    motors.setSpeeds(0, 0)
    
    while True:
        arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
        arucoParams = cv2.aruco.DetectorParameters_create()

        vid = cv2.VideoCapture(0)
        while True:
            ret, img = vid.read()
            (corners, ids, rejects) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
            #cv2.aruco.drawDetectedMarkers(image=img, corners=corners, ids=ids)
            
            if len(corners) > 0:
                
                center = (corners[0][0][0][0]+corners[0][0][2][0]) / 2
                print(center)
                
                if (center <= 319):
                    forward_right()
                elif (center > 319):
                    forward_left()
                    
            else:
                spin_left()
                        
            #cv2.imshow("detection", img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        
        vid.release()
        cv2.destroyAllWindows()
finally:  
    motors.setSpeeds(0, 0)