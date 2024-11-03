from machine import Pin, ADC
import time
		
class Potentiometer():
    pot_pin_num = None		#Pin Objects
    pot_pin_obj = None
    pot_adc 	= None
    
    ADC_MAX = 65535
    MAX_VOLTAGE = 3.3

    def __init__(self, pin, max_voltage = 3.3):
        if max_voltage <= 0:
            raise Exception("Max Voltage is not correct.")
        
        self.pot_pin_num = pin
        self.pot_pin_obj = Pin(self.pot_pin_num)
        self.pot_adc = ADC(self.pot_pin_obj)
        
        self.MAX_VOLTAGE = max_voltage

    def read_u16(self):
        return self.pot_adc.read_u16()
        
    def read_percent(self):
        raw = self.pot_adc.read_u16()
        return raw/self.ADC_MAX
    
    def read_voltage(self):
        raw = self.pot_adc.read_u16()
        return self.MAX_VOLTAGE * raw/self.ADC_MAX
        
if __name__ == '__main__':    # Program entrance
   pot = Potentiometer(26)
   while(True):
       print("16 Bit:", pot.read_u16(), "Percent:", pot.read_percent(), "Voltage:", pot.read_voltage())
       time.sleep(1)

