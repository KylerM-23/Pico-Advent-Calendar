from machine import Pin, ADC
import time
		
class Potentiometer():
    pot_pin_num = None		#Pin Objects
    pot_pin_obj = None
    pot_adc 	= None
    
    ADC_MAX = 65535
    MAX_VOLTAGE = 3.3

    def __init__(self, pin, max_voltage = 3.3):
        #

    def read_u16(self):
        #
        
    def read_percent(self):
        #
    
    def read_voltage(self):
        #
        
if __name__ == '__main__':    # Program entrance
   pot = Potentiometer(26)
   while(True):
       print("16 Bit:", pot.read_u16(), "Percent:", pot.read_percent(), "Voltage:", pot.read_voltage())
       time.sleep(1)


