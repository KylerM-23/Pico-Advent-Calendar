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
        
        self.SLOPE = math.log(self.POINTS[1][1]/self.POINTS[0][1], 10) / math.log(self.POINTS[1][0]/self.POINTS[0][0], 10)
        self.INTERCEPT = math.log(self.POINTS[1][1]/((self.POINTS[1][0]) ** self.SLOPE), 10)

    def read_voltage(self):
        return self.ldr_adc.read_u16() * self.MAX_VOLTAGE/self.ADC_MAX
    
    def read_lux(self): #rough estimate
        voltage = self.read_voltage()
        resistance = voltage * self.RESISTOR_DIVIDER/(self.MAX_VOLTAGE - voltage)
        lux = (resistance ** self.SLOPE) * (10**self.INTERCEPT)
        return lux
        
        
if __name__ == '__main__':    # Program entrance
   photoresistor = Photoresistor(27, resistor_divider = 10000)
   while(True):
       print("Voltage", photoresistor.read_voltage())
       print("Lux", photoresistor.read_lux())
       time.sleep(1)


