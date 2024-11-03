from machine import ADC, Pin
import time
from Servo import *
from Potentiometer import * 

pot = Potentiometer(26)
servo = Servo(16)

MAX_ANGLE = 180

while True:
    angle = int(pot.read_percent() * MAX_ANGLE)
    servo.move_to(angle)
    time.sleep(.1)
    print("Moving to:", angle)