from machine import Pin, PWM
from Ultrasonic_Sensor import *
from Servo import *
import time

step_size = 10
delay_time = 5 #seconds
servo = Servo(16)
us = Ultrasonic_Sensor(trig_pin = 14, echo_pin = 15)
servo.move_to(90)

while(True):
    if us.get_distance() < 15:
        for i in range(step_size):
            servo.move_by(90/step_size)
            time.sleep(0.1)
            
        time.sleep(delay_time)
        
        while(us.get_distance() < 15):
            time.sleep(0.1)
            
        for i in range(step_size):
            servo.move_by(-90/step_size)
            time.sleep(0.1)
            
#think about the program as is. is this a great gate?
#are there any feature that would improve the gate?
#what happens if someone stands at the gate and doesn't move?
#questions such as these will help guiide you into adding new features!
    
