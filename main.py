from motor import Motor
from force_sensor import Sensor
from button import Button
from display import Display
import RPi.GPIO as GPIO
import time
import sys

    
def main():
    motor=Motor()
    sensor=Sensor()
    button=Button()
    display=Display()
    #print(sensor.get_input())
    #GPIO.setup(12,GPIO.IN)
    #motor.rotate(False,2048)
    
    
    while True:
        display.print_state(button.get_state(), sensor.get_input())
        button.check_input()
        display.print_state(button.get_state(), sensor.get_input())
        if (not sensor.get_input() and button.get_state()):
            display.print_state(button.get_state(), sensor.get_input())
            motor.rotate(False,800)
            display.print_state(button.get_state(), sensor.get_input())
            time.sleep(2)
            motor.rotate(True,800)

    
try:     
    main()
except KeyboardInterrupt:
    sys.exit( 1 )