from machine import Pin
from RGB_LED import *
from Potentiometer import *
import time

pot = Potentiometer(26)
RGB = RGB_LED(R = 4, G = 5, B = 6, anode = 1, PWM_Mode = True)

ADC_MAX = 65535
division = ADC_MAX/6
slope = 255/division
    
while True:
    adc = pot.read_u16()
    
    if (adc < division):
        #
    elif (adc < 2*division):
        #
    elif (adc < 3*division):
        # 
    elif (adc < 4*division):
        #
    elif (adc < 5*division):
        #
    elif (adc < 6*division):
        #
    else:
        #
    
    RGB.set(R,G,B)
    time.sleep(.01)
