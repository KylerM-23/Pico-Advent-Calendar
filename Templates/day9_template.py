from Button_Matrix import *
from RGB_LED import *
from machine import Pin
import time

Buttons = Button_Matrix(pin_matrix = [[11,8], [12,13]])
RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1)
LED_States = [0,0,0] #RGB

button_inputs = [[0,0],[0,0]]

while True:
    for row in range(2):
        for col in range(2):
            #
            
    RGB.set(R = LED_States[0], G = LED_States[1], B = LED_States[2])
    time.sleep(0.1)