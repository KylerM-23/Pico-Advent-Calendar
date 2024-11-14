from TMP1075 import *
from Shift_Register_74_595 import *
from RGB_LED import *
from math import ceil

seven_seg = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

tmp = TMP1075(i2c_addr = 0x48, sda = 0, scl = 1)
tmp.config(mode = Continuous_Mode)
unit = 'F'

RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1)
RGB.off()

if unit == 'F':
    RGB.green(1)
elif unit == 'C':
    RGB.blue(1)

register = Shift_Register_74_595(ser_in = 21, clk = 18, latch = 19, en = [20,22], clr = 17, daisy_chain = True)
register.enable()
register.clear()
digit = 0
    
if(not(tmp.check_device_id())):
    raise Exception("Device not recongnized")

while True:
    temp = int(tmp.get_temp(unit))
    print(temp, unit)
    msd = temp//10
    lsd = ceil((temp%10)*8/10)
    
    seven_seg_reg = seven_seg[msd]
    snowflake_reg = 0xFF >> (8-lsd)
    
    register.shift_data_daisy([seven_seg_reg, snowflake_reg])
    time.sleep(1)
