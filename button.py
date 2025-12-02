import RPi.GPIO as GPIO
import time

class Button:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        self.is_activated=0
    
    def get_state(self):
        return self.is_activated
    
    def check_input(self):
        if (not GPIO.input(26)):
            self.is_activated=not self.is_activated
            time.sleep(2)
        