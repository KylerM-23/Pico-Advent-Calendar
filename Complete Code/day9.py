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
            if (Buttons.get_input(row,col) == 0 and button_inputs[row][col] != 0):
                if (row == 1 and col == 1):
                    LED_States = [0,0,0]
                else:
                    LED_States[2*row + col] = LED_States[2*row + col] ^ 1
                   
            button_inputs[row][col] = Buttons.get_input(row,col)
            
    RGB.set(R = LED_States[0], G = LED_States[1], B = LED_States[2])
    time.sleep(0.1)
    #print(buttons)
