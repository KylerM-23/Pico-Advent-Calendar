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
        RGB.set(R = 1, G = 0, B = 0)
    elif (color == 1):
        RGB.set(R = 0, G = 1, B = 0)
    elif (color == 2):
        RGB.set(R = 0, G = 0, B = 1)
    else:
        RGB.set(R = 1, G = 1, B = 1)
        
    ref_time = time.time()
    
    while ((time.time() - ref_time < difficulty) and color_selected < 0):
        for row in range(2):
            for col in range(2):
                if (Buttons.get_input(row,col) == 0 and button_inputs[row][col] != 0):
                    color_selected = 2*row + col
                button_inputs[row][col] = Buttons.get_input(row,col)
                
    if ((simon_said == 1 and color_selected == color) or (simon_said == 0 and color_selected == -1)):
        Buzzer.value(1 & sound)
        time.sleep(0.1)
        points += 1
        print ("Correct! Points:", points)
    else:
        Buzzer.value(1 & sound)
        time.sleep(0.05)
        Buzzer.value(0)
        time.sleep(0.05)
        Buzzer.value(1 & sound)
        time.sleep(0.05)
        
        if (simon_said == 0):
            print ("Incorrect Time. Points:", points)
        else:
            print ("Incorrect Color. Points:", points)
            
    Buzzer.value(0)
    RGB.set(R = 0, G = 0, B = 0)
    Simon_LED.value(0)
    time.sleep(random.randint(1,3))     