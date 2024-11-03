from machine import Pin
import time
from RGB_LED import *
import random

RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1)

while(True):
    R = random.randint(0,1)		#Pick random colors
    G = random.randint(0,1)		#for Red, Green, and
    B = random.randint(0,1)		#blue
    RGB.set(R, G, B)
    time.sleep(1)