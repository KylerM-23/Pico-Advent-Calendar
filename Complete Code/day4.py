from machine import Pin
import time

BTN = Pin(7, Pin.IN) 	#setup the push button as an input
LED = Pin(2, Pin.OUT) 	#setup the onboard LED as an output

btn_read = 0

while(True):
    btn_read = BTN.value()
    LED.value(btn_read)	#change the state of the LED pin
    time.sleep(0.5)		#wait one second