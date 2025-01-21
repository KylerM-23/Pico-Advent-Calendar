from machine import Pin
import time, random

LED = Pin(2, Pin.OUT) 		#setup the LED as an output
TS = Pin(15, Pin.IN) 		#setup the slide switch as an input

ts_read = 0
taps = 0
playing = False

def score(pin):
    global taps, playing
    
    if playing:
        taps += 1
        LED.toggle()		#change the LED
    
TS.irq(trigger=Pin.IRQ_FALLING,handler = score)

while(True):
    playing = False
    taps = 0
    print("Ready")
    time.sleep(1)		#wait
    print("Set")
    
    time.sleep(random.randint(1,4))		#wait
    playing = True
    print("GO!")
    
    time.sleep(10)		#wait
    print("You tapped:", taps, "times!")
    time.sleep(1)
