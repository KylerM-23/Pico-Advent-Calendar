from machine import Pin
import time

class Shift_Register_74_595:
    SER  	= Pin(21, Pin.OUT) 		#setup 
    CLK 	= Pin(18,  Pin.OUT)		#setup
    LATCH 	= Pin(19,  Pin.OUT)		#setup
    EN 		= Pin(20,  Pin.OUT)		#setup
    CLR		= Pin(17,  Pin.OUT)		#setup

    def __init__(self, ser_in, clk, latch, en, clr):
        self.SER  	= Pin(ser_in, Pin.OUT) 	#setup 
        self.CLK 	= Pin(clk, Pin.OUT)		#setup
        self.LATCH 	= Pin(latch, Pin.OUT)	#setup
        self.EN 	= Pin(en, Pin.OUT)		#setup
        self.CLR	= Pin(clr, Pin.OUT)		#setup
     
    def enable(self):
        #
        
    def disable(self):
        #
                     
    def clear(self):
        #
        
    def shift_data(self,write_val):
        #
        
    def run_pattern(self, patterns, delay = 1):
        #

if __name__ == '__main__':    # Program entrance
   register = Shift_Register_74_595(ser_in = 21, clk = 18, latch = 19, en = 20, clr = 17)
   register.enable()
   register.clear()
   
   while(True):
       register.shift_data(0x55)
       time.sleep(0.5)
       register.shift_data(0xAA)
       time.sleep(0.5)
