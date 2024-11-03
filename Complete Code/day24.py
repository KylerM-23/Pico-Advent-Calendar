from time import sleep, ticks_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
from Thermistor import Thermistor
from TMP1075 import *

DEFAULT_I2C_ADDR = 0x27

lcd = I2cLcd(sda = 0, scl = 1, freq = 400000, i2c_addr = DEFAULT_I2C_ADDR, num_lines = 2, num_columns = 16)
tmp = TMP1075(i2c_addr = 0x48, sda = 0, scl = 1)
thermistor = Thermistor(28, resistor_divider = 10000)

lcd.clear()
count = 0
tmp.config(mode = Continuous_Mode)

tmp1075_temp = 0
thermistor_temp = 0

while True:
    thermistor_temp = round(thermistor.get_temp('F'), 2)
    tmp1075_temp = round(tmp.get_temp('F'), 2)
    lcd.move_to(0, 0)
    lcd.putstr(f"RTH: {thermistor_temp}F\n")
    lcd.putstr(f"TMP: {tmp1075_temp}F")
    sleep(1)
    lcd.clear()