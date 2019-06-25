#!/usr/bin/env python
# this script will show a scrolling message on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
import time
#use RGB values to define colors
yellow = (102, 0, 204)
blue = (255, 255, 0)

speed = 0.05 

message = "Hello World!"

sense.show_message(message , speed, text_colour=yellow, back_colour=blue)

sense.clear()


