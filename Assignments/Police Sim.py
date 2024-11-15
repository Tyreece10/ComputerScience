from adafruit_circuitplayground import cp
import time

while True:

    cp.pixels.fill((255, 0, 0))  # Red
    cp.play_tone(500, 0.5)
    time.sleep(0.5)              # Wait


    cp.pixels.fill((0, 0, 255))  # Blue
    cp.play_tone(900, 0.5)       
    time.sleep(0.5)              # Wait