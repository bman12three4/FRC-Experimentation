#!/usr/bin/python

import time

import AdafruitCharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1, 1, 1)
lcd.clear()
lcd.message("Initializing...")
