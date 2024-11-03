from machine import Pin
import time

LED = Pin(2, Pin.OUT)    	     	#setup the LED as an output
BTN = Pin(7, Pin.IN)         		#setup the push button as an input
SW 	= Pin(3, Pin.IN, Pin.PULL_DOWN) #setup the Slide Switch as an input

while(True):
    if(SW.value() == 1):
        LED.value(BTN.value())     	#change the LED based on the button
    else:
        LED.value(0)     			#turn the LED off
	time.sleep(0.1)   	           	#wait