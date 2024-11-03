from machine import Pin
import time

class RGB_LED():
    LED_Pins_Num = [] 	#Pin Numbers in R, G, B order
    LED_Pins = []		#Pin Objects in R, G, B order
    
    polarity = 0		#Stores if we have inverted logic
    
    def __init__(self, R = 0, G = 0, B = 0, anode = 0): #by default common cathode
        #store pin numbers
        
        #create pins
        
        #turn off LED
            
    def set(self, R, G, B):
        #set each LED
    
    def white(self):
        #turn on all LEDs
      
    def off(self):
        #turn off LED
            
    def red(self, R):
        #
            
    def green(self, G):
        #
    
    def blue(self, B):
        #
        
if __name__ == '__main__':    # Program entrance
    print ('Demo Code for Common Anode RGB LED')
    RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1)
    time.sleep(1)
    
    RGB.set(R = 1, G = 0, B = 0)
    time.sleep(1)
    
    RGB.white()
    time.sleep(1)
    
    RGB.off()
    time.sleep(1)
    
    RGB.blue(B = 1)
    time.sleep(1)
    
    RGB.green(G = 1)
    time.sleep(1)
    
    RGB.off()
    time.sleep(1)