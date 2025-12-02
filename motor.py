import RPi.GPIO as GPIO
import time

class Motor:
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    step_sleep = 0.002
    step_count = 4096 #360 deg = 4096
    deg_divider=2
    rotation_deg=step_count/deg_divider
    direction = False
    step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        # setting up
        GPIO.setup( self.in1, GPIO.OUT )
        GPIO.setup( self.in2, GPIO.OUT )
        GPIO.setup( self.in3, GPIO.OUT )
        GPIO.setup( self.in4, GPIO.OUT )
        # initializing
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        self.motor_pins = [self.in1,self.in2,self.in3,self.in4]
        self.motor_step_counter = 0

    def rotate(self):
        for i in range(int(self.rotation_deg)):
            for pin in range(0, len(self.motor_pins)):
                GPIO.output( self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin] )
            if self.direction==True:
                self.motor_step_counter = (self.motor_step_counter - 1) % 8
            elif self.direction==False:
                self.motor_step_counter = (self.motor_step_counter + 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                #cleanup()
                exit( 1 )
            time.sleep( self.step_sleep )
            
    def rotate(self,direction,angle):
        for i in range(int(angle)):
            for pin in range(0, len(self.motor_pins)):
                GPIO.output( self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin] )
            if direction==True:
                self.motor_step_counter = (self.motor_step_counter - 1) % 8
            elif direction==False:
                self.motor_step_counter = (self.motor_step_counter + 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                #cleanup()
                exit( 1 )
            time.sleep(self.step_sleep)
