from __future__ import print_function
import time
from gpiozero import LED, PWMLED, Button
from time import sleep
from signal import pause

GREEN = PWMLED(21, frequency=1000)
YELLOW = LED(20)
RED = LED(19)
BLUE = LED(16)
b1 = Button(7, hold_time=3)
tc = 0


duty_cycles = list(range(0, 101)) + list(range(100, -1, -1))
i = 0
FLAG = False
run_time = 0

try:
    
    RED.on()
    time.sleep(1)
    RED.off()
    time.sleep(0.5)
    YELLOW.on()
    time.sleep(2)
    YELLOW.off()
    time.sleep(0.5)
    BLUE.on()
    time.sleep(3)
    BLUE.off()
    time.sleep(0.5)
    GREEN.on()
    time.sleep(4)
    GREEN.off()
    time.sleep(0.5)
    RED.on()
    YELLOW.on()
    BLUE.on()
    GREEN.on()
    time.sleep(0.5)
    RED.off()
    YELLOW.off()
    BLUE.off()
    GREEN.off()
    time.sleep(0.5)
    RED.on()
    YELLOW.on()
    BLUE.on()
    GREEN.on()
    time.sleep(0.5)
    RED.off()
    YELLOW.off()
    BLUE.off()
    GREEN.off()
    time.sleep(0.5)
    RED.on()
    YELLOW.on()
    BLUE.on()
    GREEN.on()
    time.sleep(0.5)
    RED.off()
    YELLOW.off()
    BLUE.off()
    GREEN.off()
    time.sleep(0.5)
    RED.on()
    YELLOW.on()
    BLUE.on()
    GREEN.on()
    time.sleep(0.5)
    RED.off()
    YELLOW.off()
    BLUE.off()
    GREEN.off()
    time.sleep(0.5)
    while True:
        
        if b1.is_pressed:
            print("Play/Pause pressed")
            b1.wait_for_release()
            print("Play/Pause released")
            FLAG = not FLAG
        if FLAG:
            #Playing mode
            start_time = time.time()
            GREEN.value = 1
            time.sleep(0.02)
            run_time += (time.time() - start_time)
            print(run_time)
            if run_time >= 10:
                YELLOW.on()
            if run_time >= 20:
                for _ in range(10):
                    RED.on()
                    time.sleep(0.5)
                    RED.off()
                    time.sleep(0.5)
                break
        else:
            #pause mode
            GREEN.value = duty_cycles[i] / 100
            time.sleep(0.02)
            i += 1
            if i >= len(duty_cycles):
                i = 0
finally:
    GREEN.off()
    YELLOW.off()
    RED.off()
    BLUE.off()