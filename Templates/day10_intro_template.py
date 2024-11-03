from Button_Matrix import *
from RGB_LED import *
from machine import Pin
import time
import random

Buttons = Button_Matrix(pin_matrix = [[11,8], [12,13]])
RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1)
LED_States = [0,0,0] #RGB
Simon_LED = Pin(2, Pin.OUT)

button_inputs = [[0,0],[0,0]]
points = 0

while True:
	color = random.randint(0,3)
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
    
	while (color_selected < 0):
    	#

	if (color_selected == color):
    	#
	else:
        #

	RGB.set(R = 0, G = 0, B = 0)
	time.sleep(random.randint(1,3))	 