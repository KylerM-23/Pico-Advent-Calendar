from machine import Pin
import utime

class Ultrasonic_Sensor():
    trigger 	= None
    echo 		= None
    time_out 	= 10**4 #10ms ~3.43 meters

    def __init__(self, trig_pin = 0, echo_pin = 0, time_out_val = None):
        self.trigger = Pin(trig_pin, Pin.OUT)
        self.echo 	 = Pin(echo_pin, Pin.IN)
        
        if time_out_val != None:
            self.time_out = time_out_val
    
    def get_distance(self):
        #
        
if __name__ == "__main__":
    us = Ultrasonic_Sensor(trig_pin = 14, echo_pin = 15)
    
    while True:
        print("Distance:", us.get_distance(),"cm")
        utime.sleep(1)
