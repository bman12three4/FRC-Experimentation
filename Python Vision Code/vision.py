#!/usr/bin/python

import time

import AdafruitCharLCD as LCD
import cv2
import numpy as np


lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1, 1, 1)

def log(string):
    lcd.clear()
    lcd.message(string)
    print(string)

lcd.clear()
lcd.message("Initializing...")
camera_port = 0 # Which port the camera is connected to.
ramp_frames = 30 # The number of frames before the camera takes the picture
camera = cv2.VideoCaptrue(camera_port) # creates the camera on the right port.
time.sleep(1) # sleeps so that you can read the message

# these are just some debug options to let you know what some of the
# values are without having to look at the code, usefull if you are
# more focussed on developing java code for the robot.
lcd.clear()
lcd.message("Camera_Port:\n")
lcd.message(camera_port)
time.sleep(0.5)

lcd.clear()
lcd.message("Ramp Frames:\n")
lcd.message(ramp_frames)
time.sleep(0.5)

def read_camera(): #gets an image from the camera
    retval, im = camera.read()
    return im

def get_image(): #gets the final image to be used by the rest of the program.
    for i in xrange(ramp_frames):
        temp = read_camera()
    log("Getting\nimage...")
    camera_capture = read_camera()
    file = "/home/pi/frc.png" #This is what needs to be changed to ram later,
                              #having all the writes to the SD card can cause it
                              #to fail after a while.
    cv2.imwrite(file, camera_capture)
