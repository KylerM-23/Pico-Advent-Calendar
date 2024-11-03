from Photoresistor import Photoresistor
from machine import Pin
import time

photoresistor = Photoresistor(27)
led = Pin(2, Pin.OUT)
led.value(0)

threshold_voltage = 2.3

while True:
    voltage = photoresistor.read_voltage()
    print(voltage)
    time.sleep(0.1)
    if voltage > threshold_voltage:
        led.value(1)
    else:
        led.value(0)