import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
led = GPIO.PWM(18,100)
led.start(0)

while True:
    for i in range(0, 100):
        led.ChangeDutyCycle(i)
        time.sleep(0.02)
    
    for i in range(100, -1, -1):
        led.ChangeDutyCycle(i)
        time.sleep(0.01)
    time.sleep(1)
        
