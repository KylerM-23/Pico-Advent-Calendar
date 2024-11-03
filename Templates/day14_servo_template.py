from machine import Pin, PWM
import time
		
class Servo():
    servo_pin_num = None		#Pin Objects
    servo_pin_obj = None
    servo_pin_pwm = None
    
    PWM_MAX = 65025
    position = 0
    
    MAX_ANGLE = 180
    MIN_ANGLE = 0

    def __init__(self, pin):
        self.servo_pin_num = pin
        self.servo_pin_obj = Pin(self.servo_pin_num)
        self.servo_pin_pwm = PWM(self.servo_pin_obj)
        self.servo_pin_pwm.freq(50)

    def move_to(self, angle):
        #
        
    def move_by(self, inc_angle):
        #
        
if __name__ == '__main__':    # Program entrance
   servo = Servo(16)
   while(True):
       servo.move_to(0)
       for i in range (0,180):
           #servo.move_to(i)
           servo.move_by(2)
           time.sleep(0.01)

