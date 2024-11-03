from machine import Pin
from Shift_Register_74_595 import *
import time

snow_flake = Shift_Register_74_595(ser_in = 21, clk = 18, latch = 19, en = 20, clr = 17)
snow_flake.enable()
snow_flake.clear()

alternating = [0xAA, 0x55]
spin_around = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

while(True):
    for i in range(5):
        snow_flake.run_pattern(alternating)
    time.sleep(1)
    for i in range(5):
        snow_flake.run_pattern(spin_around, 0.1)
    time.sleep(1)
