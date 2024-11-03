from Shift_Register_74_595 import Shift_Register_74_595
import time
from machine import Pin

seven_seg = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

BTN = Pin(7, Pin.IN) 	#setup the push button as an input

register = Shift_Register_74_595(ser_in = 21, clk = 18, latch = 19, en = [20,22], clr = 17, daisy_chain = True)
register.enable()
register.clear()
digit = 0

time_stamp = 0
time_btn_stamp = 0

run = True

while(True):
    if (BTN.value() and time.time() - time_btn_stamp >= 1):
        run = run ^ 1
        time_btn_stamp = time.time()
        time_stamp = time.time()
    if (run):
        if (time.time() - time_stamp >= 1):
            register.shift_data_daisy([seven_seg[digit], digit])
            digit+=1 
            if (digit > 15):
                digit = 0
            time_stamp = time.time()
    
