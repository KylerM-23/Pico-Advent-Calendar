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
        R = 255
        G = slope * (adc)
        B = 0
    elif (adc < 2*division):
        R = -slope * (adc - division) + 255
        G = 255
        B = 0
    elif (adc < 3*division):
        R = 0
        G = 255
        B = slope * (adc - 2 * division) 
    elif (adc < 4*division):
        R = 0
        G = -slope * (adc - 3 * division) + 255
        B = 255
    elif (adc < 5*division):
        R = slope * (adc - 4 * division)
        G = 0
        B = 255
    elif (adc < 6*division):
        R = 255
        G = 0
        B = -slope * (adc - 5 * division) + 255
    else:
        R = 255
        G = 0
        B = 0
    
    RGB.set(R,G,B)
    time.sleep(.01)