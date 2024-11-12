from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch:  # Check if the switch is to the right (True)
        for i in range(5):
            cp.pixels[i] = (0, 0, 0)  # Turn off pixels 0-4
        for i in range(5, 10):
            cp.pixels[i] = (0, 1, 0)  # Turn on pixels 5-9 to green
    else:  # Switch is to the left
        for i in range(5):
            cp.pixels[i] = (0, 1, 0)  # Turn on pixels 0-4 to green
        for i in range(5, 10):
            cp.pixels[i] = (0, 0, 0)  # Turn off pixels 5-9
