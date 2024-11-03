from machine import Pin, ADC
import time, math
		
class Photoresistor():
    ldr_pin_num = None		#Pin Objects
    ldr_pin_obj = None
    ldr_adc 	= None
    
    ADC_MAX = 65535
    MAX_VOLTAGE = 3.3
    RESISTOR_DIVIDER = 10000
    SLOPE = 0
    INTERCEPT = 0
    POINTS = [(10*10**3, 10),(10**3, 100)] #Put points to define the photoresistor

    def __init__(self, pin, max_voltage = 3.3, resistor_divider = 10000):
        if max_voltage <= 0:
            raise Exception("Max Voltage is not correct.")
        if resistor_divider <= 0:
            raise Exception("Resistor Divider is not correct.")
        
        self.ldr_pin_num = pin
        self.ldr_pin_obj = Pin(self.ldr_pin_num)
        self.ldr_adc = ADC(self.ldr_pin_obj)
        
        self.MAX_VOLTAGE = max_voltage
        self.RESISTOR_DIVIDER = resistor_divider
        
        #

    def read_voltage(self):
        #
    
    def read_lux(self): #rough estimate
        #
        
if __name__ == '__main__':    # Program entrance
   photoresistor = Photoresistor(27, resistor_divider = 10000)
   while(True):
       print("Voltage", photoresistor.read_voltage())
       print("Lux", photoresistor.read_lux())
       time.sleep(1)


