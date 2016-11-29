#!/usr/bin/python

import time
import socket

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
UDP_IP = "10.54.82.1" #change this to the actual ip later
UDP_PORT = 5482
MESSAGE = "0x0"
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

lcd.clear()
lcd.message("UDP target ip:\n")
lcd.message(UDP_IP)
time.sleep(0.5)

lcd.clear()
lcd.message("UDP target port:\n")
lcd.message(UDP_PORT)
lcd.sleep(0.5)

lcd.clear()
lcd.message("Initializing\nDone!")
lcd.sleep(1)


def read_camera(): #gets an image from the camera
    retval, im = camera.read()
    return im

def get_image(): #gets the final image to be used by the rest of the program.
    for i in xrange(ramp_frames):
        temp = read_camera()
    log("Getting\nimage...")
    camera_capture = read_camera()
    #file = "/home/pi/frc.png" #This is what needs to be changed to ram later,
                              #having all the writes to the SD card can cause it
                              #to fail after a while.
    #cv2.imwrite(file, camera_capture)
    retval, img = camera_capture #Change the return value to the image,
                                 #rather then creating another file each time.
    return img #return the image


