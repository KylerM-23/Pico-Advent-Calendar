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
        if (angle > self.MAX_ANGLE):
            angle = self.MAX_ANGLE
        elif (angle < self.MIN_ANGLE):
            angle = self.MIN_ANGLE
            
        dc = int((angle/18 + 2.5) * self.PWM_MAX / 100)
        self.servo_pin_pwm.duty_u16(dc)
        self.position = angle
        
    def move_by(self, inc_angle):
        angle = self.position + inc_angle
        self.move_to(angle)
        
        
if __name__ == '__main__':    # Program entrance
   servo = Servo(16)
   while(True):
       servo.move_to(0)
       for i in range (0,180):
           #servo.move_to(i)
           servo.move_by(2)
           time.sleep(0.01)
