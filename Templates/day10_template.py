from Button_Matrix import *
from RGB_LED import *
from machine import Pin
import time
import random

Buttons = Button_Matrix(pin_matrix = [[11,8], [12,13]])
RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1)
LED_States = [0,0,0] #RGB
Simon_LED = Pin(2, Pin.OUT)
Buzzer = Pin(10, Pin.OUT)
Audio_SW = Pin(3, Pin.IN, Pin.PULL_DOWN) #setup the Slide Switch as an input

simon_probability = 0.1
difficulty = 3

button_inputs = [[0,0],[0,0]]
points = 0

sound = 1

while True:
    sound = Audio_SW.value()
    color = random.randint(0,3)
    simon_said = 1 if random.random() > simon_probability else 0
    Simon_LED.value(simon_said)
    color_selected = -1
    
    if (color == 0):
        #
    elif (color == 1):
        #
    elif (color == 2):
        #
    else:
        #
        
    ref_time = time.time()
    
    while ((time.time() - ref_time < difficulty) and color_selected < 0):
        #
    
    
    if ((simon_said == 1 and color_selected == color) or (simon_said == 0 and color_selected == -1)):
        #
    else:
        #
            
    Buzzer.value(0)
    RGB.set(R = 0, G = 0, B = 0)
    Simon_LED.value(0)
    time.sleep(random.randint(1,3))     
