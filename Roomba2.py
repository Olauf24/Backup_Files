from __future__ import print_function
import time
from dual_mc33926_rpi import motors, MAX_SPEED
from gpiozero import LED, PWMLED, Button, DistanceSensor, PhaseEnableRobot
from time import sleep
from signal import pause

GREEN = PWMLED(21, frequency=1000)
YELLOW = LED(20)
RED = LED(19)
b1 = Button(27, hold_time=3)
sensor = DistanceSensor(18, 17)
motor_1 = LED(24)
motor_2 = LED(25)


duty_cycles = list(range(0, 101)) + list(range(100, -1, -1))
i = 0
FLAG = False
run_time = 0

#Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 400 + list(range(MAX_SPEED, 0, -1)) + [0]  

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 400 + list(range(-MAX_SPEED, 0, 1)) + [0]  

try:
    motors.enable()
    motors.setSpeeds(0, 0)
    
    while True:
        
            #Playing mode
        if sensor.distance >= 0.2:    
            GREEN.on()    
            motors.motor1.setSpeed(MAX_SPEED)
            motors.motor2.setSpeed(MAX_SPEED)
            time.sleep(0.05)
        if sensor.distance < 0.2:
            motors.motor1.setSpeed(-MAX_SPEED)
            motors.motor2.setSpeed(-MAX_SPEED)
            GREEN.off()
            time.sleep(0.05)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)
  motors.disable()