from adafruit_circuitplayground import cp
import time

pixels = 0


while True:
    if cp.button_a:
        if pixels < 10:
            cp.pixels[pixels] = (0, 0, 1) 
            pixels += 1
        time.sleep(0.2)

    if cp.button_b:
        if pixels > 0:
            pixels -= 1
            cp.pixels[pixels] = (0, 0, 0)
        time.sleep(0.2)

    time.sleep(0.1)

