# Pico-Advent-Calendar

## Introduction
The 25 Days of Makermas is a Raspberry Pi Pico kit consiting of 25 projects that serve as an introduction to programming and controlling devices with a Raspberry Pi Pico.

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
- Day 1
- Day 2
- Day 3
- Day 4
- Day 5
- Day 6

## Day 1: Setup
1. Thonny IDE
   1. Install Thonny
   2. Download Pi Pico Firmware
   3. Run Test Program
2. The Pi Pico Pinout
   1. Pinout
   2. Identify GPIO pin for LED
3. Demo Program
  
### Thonny IDE
Go to the [Thonny](https://thonny.org/) website and download the free IDE. Thonny was chosen because it has features that make it easier to program with the pico and installing the firmware.

After opening Thonny, go to _Run_ -> _Configure Interpreter_                                                                   </br> <img height = "350" src = "Image/Thonny/Main_Page.jpg"></br> 
From the Interpreter Menu Select _MicroPython (Raspberry Pi Pico)_ and click on __Install or update MicroPython__              </br> <img height = "350" src = "Image/Thonny/Options.jpg"> </br> 
Copy the following settings to install the Pi Pico Firmware. _If you have a different Pico model, choose the proper variant._  </br> <img height = "350" src = "Image/Thonny/Firmware_Settings.jpg"></br> 
The Pico should be ready to go.

