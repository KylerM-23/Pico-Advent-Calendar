from WeWishYouAMerryChristmas import *
from Potentiometer import *

mP = WeWishYouAMerryChristmas(9, tempo = 140, volume = 50)
vol = 50
pot = Potentiometer(26)

BTN = Pin(7, Pin.IN) 	#setup the push button as an input
refTime = 0
play = True
done = False

def play_pause(pin):
    global play, refTime

    if (time.time() - refTime > 0.25):
        play = not(play)
        refTime = time.time()
        mP.stop()
    
BTN.irq(trigger=Pin.IRQ_RISING,handler = play_pause)

while (done == False):
    if (play):
        vol = pot.read_percent() * 100
        if (vol < 10):
            vol = 0
        elif (vol >= 90):
            vol = 90
        print(vol)
        mP.setVolume(vol)
        done, delay = mP.nextNote()
        print(done, delay)
        sleep_ms(delay)
mP.stop()
