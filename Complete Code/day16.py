from machine import Pin
import time

ALARM  		= Pin(10, Pin.OUT) 		#setup the Buzzer as an input
LED 		= Pin(2,  Pin.OUT)		#setup the LED as an output
IR_SENSOR 	= Pin(14, Pin.IN) 		#setup the IR sensor as an input
BTN  		= Pin(7,  Pin.IN) 		#setup the Button as an output

alarm_triggered = False
hold_trigger = False

while(True):
    if (IR_SENSOR.value() == 1):
        ALARM.value(1)
        LED.value(1)
        alarm_triggered = True
    else:
        if (hold_trigger == False):
            ALARM.value(0)
    
    if (BTN.value() == 1):
        alarm_triggered = False
        ALARM.value(0)
        LED.value(0)
