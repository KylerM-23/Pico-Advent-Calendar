from machine import Pin
import time

Buzzer = Pin(10, Pin.OUT) 	#setup the buzzer
BTN = Pin(7, Pin.IN) 		#setup the button as an input

pressed = False

while True:
    if(BTN.value() == 1 and pressed == False):
        Buzzer.value(1)        	#toggle the state of the LED pin
        pressed = True
    elif(BTN.value() == 0 and pressed == True):
        Buzzer.value(0)        	#toggle the state of the LED pin
        time.sleep(1)
        pressed = False
