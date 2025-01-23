from machine import Pin
import time

Buzzer = Pin(10, Pin.OUT) 	#setup the buzzer
BTN = Pin(7, Pin.IN) 		#setup the button as an input

timer = time.time()
pressed = False

while True:
    if(BTN.value() == 1 and (time.time() - timer > 1)):
        Buzzer.value(1)        	#turn on the buzzer
        pressed = True
        timer = time.time()
    elif(BTN.value() == 0 and pressed == True):
        Buzzer.value(0)        	#turn off the buzzer
        time.sleep(1)
        pressed = False