from adafruit_circuitplayground import cp
import time

while True:
    # Flash all pixels red
    cp.pixels.fill((255, 0, 0))
    cp.play_tone(500, 0.5)       # 500 Hz tone for 0.5 seconds
    time.sleep(0.5)              # Wait 0.5 seconds
    
    # Flash all pixels blue
    cp.pixels.fill((0, 0, 255))
    cp.play_tone(900, 0.5)       # 900 Hz tone for 0.5 seconds
    time.sleep(0.5)              # Wait 0.5 seconds