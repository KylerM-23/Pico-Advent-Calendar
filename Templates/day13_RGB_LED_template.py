from machine import Pin, PWM
import time

class RGB_LED():
    LED_Pins_Num = [] 	#Pin Numbers in R, G, B order
    LED_Pins = []		#Pin Objects in R, G, B order
    
    PWM_Mode = False
    PWM_MAX = 65025
    
    polarity = 0		#Stores if we have inverted logic
    
    def __init__(self, R = 0, G = 0, B = 0, anode = 0, PWM_Mode = False): #by default common cathode & not PWM
        self.LED_Pins_Num = [R, G, B] 					#store pin numbers
        self.LED_Pins = []
        self.polarity = anode
        self.PWM_Mode = PWM_Mode
        
        for pin in self.LED_Pins_Num:					#create pins
            if (self.PWM_Mode):
                #
            else:
                pin_obj = Pin(pin, Pin.OUT)
            
            self.LED_Pins.append(pin_obj)
        
        self.off()						                #turn off LED
    
    def change_pin_mode(self, PWM_Mode):
        #
        
    def set(self, R, G, B):					#if PWM, RGB values are 8 bit
        for i, color in enumerate([R,G,B]):
            if (self.PWM_Mode):
                #
            else:
                self.LED_Pins[i].value(color^self.polarity)
    
    def white(self):
        for LED in self.LED_Pins:						#turn on LED
            if (self.PWM_Mode):
                #
            else:
                LED.value(self.polarity ^ 1)
      
    def off(self):
        for LED in self.LED_Pins:						#turn off LED
            if (self.PWM_Mode):
                #
            else:
                LED.value(self.polarity ^ 0)
            
    def red(self, R):
        if (self.PWM_Mode):
            #
        else:
            self.LED_Pins[0].value(R^self.polarity)
            
    def green(self, G):
        if (self.PWM_Mode):
            #
        else:
            self.LED_Pins[1].value(G^self.polarity)
    
    def blue(self, B):
        if (self.PWM_Mode):
            #
        else:            
            self.LED_Pins[2].value(B^self.polarity)
        
if __name__ == '__main__':    # Program entrance
    print ('Demo Code for Common Anode RGB LED')
    RGB = RGB_LED(R = 4,G = 5,B = 6, anode = 1, PWM_Mode = True)
    time.sleep(1)
    
    RGB.set(R = 145, G = 0, B = 100)
    time.sleep(1)
    
    RGB.white()
    time.sleep(1)
    
    RGB.off()
    time.sleep(1)
    
    RGB.blue(B = 100)
    time.sleep(1)
    
    RGB.green(G = 101)
    time.sleep(1)
    
    RGB.change_pin_mode(PWM_Mode = False)
    RGB.off()
    time.sleep(1)