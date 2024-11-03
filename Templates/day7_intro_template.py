from machine import Pin
import time

LED = Pin(2, Pin.OUT) 		#setup the LED as an output
TS = Pin(15, Pin.IN) 		#setup the slide switch as an input

ts_read = 0
taps = 0
previous_state = False

while(True):
    #