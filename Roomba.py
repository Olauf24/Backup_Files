from __future__ import print_function
import time
from dual_mc33926_rpi import motors, MAX_SPEED
from gpiozero import LED, PWMLED, Button, PhaseEnableRobot
from time import sleep
from signal import pause

GREEN = PWMLED(21, frequency=1000)
YELLOW = LED(20)
RED = LED(19)
b1 = Button(7, hold_time=3)
sensor = DistanceSensor(18, 17)
motor_1 = LED(24)
motor_2 = LED(25)
tc = 0


duty_cycles = list(range(0, 101)) + list(range(100, -1, -1))
i = 0
FLAG = False
run_time = 0

#Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 400 + list(range(MAX_SPEED, 0, -1)) + [0]  

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 400 + list(range(-MAX_SPEED, 0, 1)) + [0]
#motor 2 is backwards

try:
    motors.enable()
    motors.setSpeeds(0, 0)
    
    while True:
        
        if b1.is_pressed:
            print("Play/Pause pressed")
            b1.wait_for_release()
            print("Play/Pause released")
            FLAG = not FLAG
        if FLAG:
            #Playing mode
            start_time = time.time()
            if sensor.distance >= 0.6:    
                GREEN.on()    
                motors.motor1.setSpeed(250)
                motors.motor2.setSpeed(250)
                time.sleep(0.05)
            if sensor.distance < 0.6:
                motors.motor1.setSpeed(250)
                motors.motor2.setSpeed(-250)
                GREEN.off()
                time.sleep(0.05)
            run_time += (time.time() - start_time)
            print(run_time)
            if run_time >= 60:
                YELLOW.on()
            if run_time >= 90:
                motors.setSpeeds(0, 0)
                for _ in range(10):
                    RED.on()
                    time.sleep(0.5)
                    RED.off()
                    time.sleep(0.5)
                break
        else:
            #pause mode
            motors.setSpeeds(0, 0)
            GREEN.value = duty_cycles[i] / 100
            time.sleep(0.02)
            i += 1
            if i >= len(duty_cycles):
                i = 0
finally:
    GREEN.off()
    YELLOW.off()
    RED.off()
    motors.setSpeeds(0, 0)