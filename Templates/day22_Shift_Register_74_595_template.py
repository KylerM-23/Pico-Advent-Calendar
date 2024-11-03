from machine import Pin
import time

class Shift_Register_74_595:
    SER  	= Pin(21, Pin.OUT) 		#setup 
    CLK 	= Pin(18,  Pin.OUT)		#setup
    LATCH 	= Pin(19,  Pin.OUT)		#setup
    EN 		= Pin(20,  Pin.OUT)		#setup
    CLR		= Pin(17,  Pin.OUT)		#setup
    
    daisy_chain = False
    EN_List = []

    def __init__(self, ser_in, clk, latch, en, clr, daisy_chain = False):
        self.SER  	= Pin(ser_in, Pin.OUT) 	#setup 
        self.CLK 	= Pin(clk, Pin.OUT)		#setup
        self.LATCH 	= Pin(latch, Pin.OUT)	#setup
        
        if(daisy_chain):
            #
        else:
            self.EN = Pin(en, Pin.OUT)		#setup
            
        self.CLR = Pin(clr, Pin.OUT)		#setup
     
    def enable(self):
        if self.daisy_chain:
            #
        else:
            self.EN.value(0)
        self.CLR.value(1)
        
    def disable(self):
        if self.daisy_chain:
            #
        else:
            self.EN.value(1)
                     
    def clear(self):
        self.CLR.value(0)
        time.sleep(1)
        self.CLR.value(1)
        
    def shift_data(self,write_val):
        self.LATCH.value(0)
        for i in range(8):
            self.CLK.value(0)
            val = (0x80 & (write_val << i) == 0x80)
            self.SER.value(val)
            self.CLK.value(1)
        self.LATCH.value(1)
            
    def shift_data_daisy(self, write_data):
        #
        
    def run_pattern(self, patterns, delay = 1):
        for p in patterns:
            self.shift_data(p)
            time.sleep(delay)

if __name__ == '__main__':    # Program entrance
   register = Shift_Register_74_595(ser_in = 21, clk = 18, latch = 19, en = 20, clr = 17)
   register.enable()
   register.clear()
   
   while(True):
       register.shift_data(0x55)
       time.sleep(0.5)
       register.shift_data(0xAA)
       time.sleep(0.5)