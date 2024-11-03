from machine import Pin
import time

Buzzer = Pin(10, Pin.OUT) 	#setup the buzzer
Slider = Pin(3, Pin.IN, Pin.PULL_DOWN) #setup the Slide Switch as an input

while True:
    if(Slider.value() == 1):
        Buzzer.value(1)			#toggle the state of the LED pin
        time.sleep(0.1)
        Buzzer.value(0)
        time.sleep(2)
    else:
        Buzzer.value(0) 


