from machine import Pin, PWM
from utime import sleep_ms

class Note: 			# Class to store the notes
    NOTE_LENGTH = 0 	# Use Half notes, quarter notes, etc
    TIME_LENGTH = 1		# Uses time in ms

    def __init__ (self, tone, delay = 8, length_type = NOTE_LENGTH):
        self.tone = tone
        self.duration = delay
        self.length_type = length_type
    
class Music_Player:
    buzzer = None				#object storing the pin
    note = 0					#index for the note being played
    tempo = 100					#tempo (speed) of the music in beats / minute
    volume = 1000				#volume (duty cycle) of the buzzer
    whole_note_duration = 0 	#duration of a whole note in ms 
    
    AUDIO_MAX = 3000
    
    #Dictionary of the different notes
    #Pauses/Rests are represented with a P
    tones = {"B0": 31, "C1": 33, "CS1": 35, "D1": 37, "DS1": 39,"E1": 41,
    "F1": 44, "FS1": 46, "G1": 49,"GS1": 52, "A1": 55, "AS1": 58,"B1": 62,
    "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93,
    "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123, "C3": 131,
    "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175, "FS3": 185,
    "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247, "C4": 262,
    "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370,
    "G4": 392, "GS4": 415, "A4": 440, "AS4": 466, "B4": 494, "C5": 523,
    "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740,
    "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988, "C6": 1047,
    "CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397, "FS6": 1480,
    "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976, "C7": 2093,
    "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960,
    "G7": 3136, "GS7": 3322, "A7": 3520, "AS7": 3729, "B7": 3951, "C8": 4186,
    "CS8": 4435, "D8": 4699, "DS8": 4978 }

    #example song with notes
    song = [Note("E5", 8),	Note("G5", 8),	Note("A5", 8), 	Note("P", 8),	Note("E5", 8),
            Note("G5", 8), 	Note("B5", 8), 	Note("A5", 8), 	Note("P",8), 	Note("E5",8),
            Note("G5", 8),	Note("A5", 8), 	Note("P", 8), 	Note("G5", 8),	Note("E5", 8)]

    def __init__(self, pin, tempo = 200, volume = 50):
        self.tempo = tempo
        self.whole_note_duration = 240000/self.tempo
        self.buzzer = PWM(Pin(pin))
        self.volume = volume
        
    def setBuzzer(self, frequency):
        self.buzzer.duty_u16(int(self.volume*self.AUDIO_MAX/100))	#need to set volume after a rest
        self.buzzer.freq(frequency)			#sets the freq of the note

    def setVolume(self, volume):
        self.volume = volume
        
    def stop(self):
        self.buzzer.duty_u16(0)				#turns off the volume of the buzzer
    
    def resetNote(self, noteNum = 0):
        self.note = noteNum
    
    def getDuration(self, divider, ms = True):
        delay = self.whole_note_duration/abs(divider)
        
        if (divider) < 0:
            delay *= 1.5
        return delay if ms else delay * 1000
    
    def playNote(self, note, sleep_func = False): #pass the note and specify if the function should sleep
        if (note.tone == "P"):
            self.stop()
        else:
            if (type(note.tone) == str):					#if using note notation, look it up
                self.setBuzzer(self.tones[note.tone])
            else:											#if providing the raw freq
                self.setBuzzer(note.tone)
            
        if (note.length_type == note.TIME_LENGTH):
            duration = int(note.duration)					#use the raw ms duration
        else:
            duration = int(self.getDuration(note.duration))	#calculate the duration
        
        if(sleep_func):
            sleep_ms(duration)
            
        return duration

    def play(self):
        for i in range(len(self.song)):
            currentNote = self.song[i]
            self.playNote(currentNote, True)      
        self.stop()
        
    def nextNote(self):
        currentNote = self.song[self.note]
        duration = self.playNote(currentNote)
        self.note = self.note + 1
        
        if self.note >= len(self.song):
            self.note = 0
            return True, duration
        
        return False, duration
            
if __name__ == '__main__':
    mP = Music_Player(9, tempo = 100, volume = 60)

    #mP.play()
    done = False
    while (done == False):
        done, delay = mP.nextNote()
        print(done, delay)
        sleep_ms(delay)
    mP.stop()