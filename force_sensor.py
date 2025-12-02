import RPi.GPIO as GPIO
import time

class Sensor:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.IN)
    
    def get_input(self):
        return GPIO.input(4)
      