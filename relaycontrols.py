import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pinList = [14,15]
for i in pinList:
        GPIO.setup(i, GPIO.OUT)

def switch(pin, state):
        if state == True:
                GPIO.output(pin, GPIO.HIGH)
        elif state == False:
                GPIO.output(pin, GPIO.LOW)

