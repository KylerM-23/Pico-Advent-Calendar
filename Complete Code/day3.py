from machine import Pin
import time

LED = Pin(2, Pin.OUT) 	#setup the onboard LED as an output

state = 0

while(True):
    LED.value(state)	#change the state of the LED pin
    time.sleep(1)		#wait one second
    state = ~state		#change the state