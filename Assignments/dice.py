from adafruit_circuitplayground import cp
import random
import time


while True:
    cp.pixels.brightness = 0.1  # Set brightness
    if cp.button_a:
        num_pixels = random.randint(1, 10)
        
        # Light up the number of pixels
        for i in range(num_pixels):
            cp.pixels[i] = (184, 2, 26)

        time.sleep(0.2)
    
    if cp.button_b:
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.2)
