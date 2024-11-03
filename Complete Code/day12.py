from Potentiometer import *
from machine import ADC, Pin, PWM
pot = Potentiometer(26)

PWM_MAX = 65025

led_pin = Pin(2)
led_pwm = PWM(led_pin)
led_pwm.freq(1000)					# 1KHz

while True:
    dc = int(pot.read_percent() * PWM_MAX)
    
    if dc < 1000:
        dc = 0
        
    led_pwm.duty_u16(dc)	
    time.sleep(0.05)