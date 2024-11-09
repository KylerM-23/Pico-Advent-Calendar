# Pico-Advent-Calendar

## Introduction
The 25 Days of Makermas is a Raspberry Pi Pico kit consiting of 25 projects that serve as an introduction to programming and controlling devices with a Raspberry Pi Pico. </br>

[Booklet WIP](https://docs.google.com/document/d/1rmNjlnt3vpmemfZ5pnnCj9qUnz_O2xRp1bQ-7SMrb30/edit?usp=sharing) </br> 
<img height = "350" src = "Image/Pi_Pico_Advent_Calendar.jpg"></br> 
 
## Parts Included:

| Item                           | Quantity | | Item                           | Quantity |
| ------------------------------ | -------- |-| ------------------------------ | -------- |
| Pi Pico                        | 1        | | Large Button                   | 3        |
| Makermas PCB                   | 1        | | Large Button Caps              | 3        |
| Wire M-F                       | 1        | | Slide Switch                   | 3        |
| Wire F-F                       | 1        | | Common Anode RGB LED           | 3        |
| Wire M-M                       | 1        | | White LED                      | 10       |
| 10k Potentiometer              | 2        | | Green LED                      | 10       |
| 180 Degree Servo Motor         | 1        | | HC-SR04 Ultrasonic Sensor      | 1        |
| 2.2K Resistors                 | 20       | | PIR Motion Sensor HC-SR501     | 1        |
| 10k Resistors                  | 4        | | TMP1075 I2C Module             | 1        |
| 10k Photoresistor              | 2        | | 1602 I2C LCD                   | 1        |
| 10k Thermistor                 | 2        | | Capacitive Touch Sensor Module | 1        |
| Common Anode 7-Segment Display | 2        | | 16 Pin IC Sockets              | 3        |
| 220 Ohm Resistor Array         | 4        | | 2 Pin Male Header              | 2        |
| SN74HC595 IC                   | 3        | | 2 Pin Jumper                   | 2        |
| 0.1uF Capacitor                | 4        | | 3 Pin Male Header              | 4        |
| Passive (Transducer) Buzzer    | 2        | | Popsicle Stick                 | 3        |
| Active (Indicator) Buzzer      | 2        | | Rubber Band                    | 3        |
| Small Button                   | 10       | | Micro USB Cable                | 1        |
| 3 Pin Female Header            | 2        | | 4 Pin Male Header              | 3        |
| 4 Pin Female Header            | 3        | | 5 Pin Female Header            | 3        |
| 20 Pin Female Header           | 3        | | 5 Pin Female Header            | 5        |
| Nylon Standoffs M3 x 20MM      | 5        |





## Table of Contents
- [Day 1](#day1)
- [Day 2](#day2)
- [Day 3](#day3)
- [Day 4](#day4)
- [Day 5](#day5)
- [Day 6](#day6)

## Day 1: Setup <a name="day1"></a>
1. [Thonny IDE](day1_thonny)
   1. Install Thonny
   2. Download Pi Pico Firmware
   3. Run Test Program
2. [The Pi Pico Pinout](day1_pinout)
   1. Pinout
   2. Identify GPIO pin for LED
3. [Controlling the onboard LED](day1_demo)
  
### Thonny IDE <a name="day1_thonny"></a>
Go to the [Thonny](https://thonny.org/) website and download the free IDE. Thonny was chosen because it has features that make it easier to program with the pico and installing the firmware.

After opening Thonny, go to _Run_ -> _Configure Interpreter_                                                                   </br> <img height = "350" src = "Image/Thonny/Main_Page.jpg"></br> 
From the Interpreter Menu Select _MicroPython (Raspberry Pi Pico)_ and click on __Install or update MicroPython__              </br> <img height = "350" src = "Image/Thonny/Options.jpg"> </br> 
Copy the following settings to install the Pi Pico Firmware. _If you have a different Pico model, choose the proper variant._  </br> <img height = "350" src = "Image/Thonny/Firmware_Settings.jpg"></br> 

The Pico should be ready to go. </br>

We can now use the shell and write the hardest line of code ever. </br> <img width = "600" src = "Image/Thonny/Shell.jpg"></br> 

### Pico Pinout  <a name="day1_pinout"></a>
Microcontrollers have multiple pins that have multiple functions on each. Most pins are general purpose input outpute (GPIO) pins that can be configure to output signals/data or input (recieve) signals/data. The other pins are power pins or serve special functions.
 - The power pins are VBUS (5V from the USB), 3V3 (3.3V), and GND. The other pins are power input or other functons.

Many of the GPIO pins have multiple functions that can only be used on that pin. For example Pin 32 has GP27, ADC1, and I2C1 SDA for its functions. Programmers can choose which function they want to use on each pin. How you use each pin will vary on what pin functions you need.
- For example if you need a lot of ADC functions, it may be better to use another pin's I2C function and dedicate Pin 32 to ADC.

The image below shows all the pins on the pico with their respective features. </br> <img height = "350" src = "Image/Pinout.jpg"> </br> 

### Controlling the onboard LED <a name="day1_demo"></a>
Day1.py toggles the onboard LED and you can vary the speed at which the LED blinks. If you make the time fast enough the LED will appear constantly illuminated and you cannot see it turning off.
