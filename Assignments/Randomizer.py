from adafruit_circuitplayground import cp
import time
import random

while True:
    cp.pixels.brightness = 0.1
    x, y, z = cp.acceleration
    if z <= 2:
        for i in range(10):
            colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cp.pixels[i] = colors
