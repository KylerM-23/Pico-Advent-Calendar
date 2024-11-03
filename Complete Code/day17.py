from machine import Pin, PWM
from Ultrasonic_Sensor import *
import time

us = Ultrasonic_Sensor(trig_pin = 14, echo_pin = 15)
    
PWM_MAX = 65025
DIST_MAX = 50
led = PWM(Pin(2, Pin.OUT))
led.freq(1000)

while True:
    dist = us.get_distance()
    
    dc = (1-dist/DIST_MAX) if (0 < dist < DIST_MAX) else 0 
    print("Distance:", dist, "cm", "Duty Cycle:", dc)
    led.duty_u16(int(dc * PWM_MAX))
    time.sleep(0.1)
