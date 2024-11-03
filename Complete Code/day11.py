from Potentiometer import *
from machine import Pin
import time

pot = Potentiometer(26)
led = Pin(2, Pin.OUT)

while True:
    if (pot.read_percent() >=0.5):
        led.value(1)
    else:
        led.value(0)