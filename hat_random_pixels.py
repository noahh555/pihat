#!/usr/bin/env pythong
#displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time
import random 
sense = SenseHat()

x = random.randint(0,7)
y = random.randint(0,7)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

sense.set_pixel(x, y, (r, g, b))


time.sleep(3)
sense.clear()
