from machine import Pin
import time

LED = Pin(25, Pin.OUT) 	#setup the onboard LED as an output

while(True):
    LED.toggle()		#toggle the state of the LED pin
    time.sleep(1)		#wait one second

