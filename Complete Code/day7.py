from machine import Pin
import utime

LED = Pin(2, Pin.OUT)    	     #setup the LED as an output
SW = Pin(3, Pin.IN, Pin.PULL_DOWN) #setup the Slide Switch as an input
Buzzer = Pin(10, Pin.OUT) 	#setup the buzzer

alarm_state = False #off by default
alarm_time = 10
timer = utime.time()

irq_timer = utime.ticks_ms()
irq_cooldown = 50 #500 ms cooldown
debounce_time = 10

LED.value(0)          #change the LED

def alarm_change(pin):
    global alarm_state, timer, irq_timer
    
    if (utime.ticks_ms() - irq_timer > irq_cooldown):
        irq_timer = utime.ticks_ms()
    else:
        return
    
    utime.sleep_ms(debounce_time)
    alarm_state = SW.value()
    timer = utime.time()
    
    LED.value(alarm_state)		#change the LED

SW.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = alarm_change)#, hard = True)

while(True):
    if (alarm_state and (utime.time() > (timer + alarm_time))):
        for i in range(4):
            Buzzer.value(1)
            utime.sleep(0.1)
            Buzzer.value(0)
            utime.sleep(0.2)
        timer = utime.time()