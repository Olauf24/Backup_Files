import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
    
GPIO.output(18, False)
GPIO.output(23, False)
GPIO.output(25, False)
GPIO.output(7, False)

GPIO.output(18, True)
time.sleep(1)
GPIO.output(18, False)
time.sleep(1)

GPIO.output(23, True)
time.sleep(2)
GPIO.output(23, False)
time.sleep(1)

GPIO.output(25, True)
time.sleep(3)
GPIO.output(25, False)
time.sleep(1)

GPIO.output(7, True)
time.sleep(4)
GPIO.output(7, False)
time.sleep(1)

for i in range(4):
     GPIO.output(18, True)
     GPIO.output(23, True)
     GPIO.output(25, True)
     GPIO.output(7, True)
     time.sleep(0.5)
     GPIO.output(18, False)
     GPIO.output(23, False)
     GPIO.output(25, False)
     GPIO.output(7, False)
     time.sleep(1)
     
led = GPIO.PWM(7,100)
led.start(0)
 
for i in range(0, 100):
    led.ChangeDutyCycle(i)
    time.sleep(0.02)
 
for i in range(100, -1, -1):
    led.ChangeDutyCycle(i)
    time.sleep(0.02)
time.sleep(1)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
green = GPIO.PWM(7,100)
green.start(0)

#mode=0
while True:
    if not GPIO.input(20):
        mode=mode+1
    if mode%2==0:
        green.ChangeDutyCycle(100)
        time.sleep(0.02)
    else:
        green.ChangeDutyCycle(0)
        time.sleep(0.02)


