from adafruit_circuitplayground import cp
import time

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    print(f"Temperature: {temp_f} F")

    cp.pixels.fill((0, 0, 0))

    if temp_f < 60:
        cp.pixels[0] = (0, 0, 255)
    elif temp_f > 64:
        for i in range(2):
            cp.pixels[i] = (28, 0, 227)
    elif temp_f > 68:
        for i in range(3):
            cp.pixels[i] = (57, 0, 199)
    elif temp_f > 72:
        for i in range(4):
            cp.pixels[i] = (85, 0, 170)
    elif temp_f > 76:
        for i in range(5):
            cp.pixels[i] = (113, 0, 142)
    elif temp_f > 80:
        for i in range(6):
            cp.pixels[i] = (142, 0, 113)
    elif temp_f > 84:
        for i in range(7):
            cp.pixels[i] = (170, 0, 85)
    elif temp_f > 88:
        for i in range(8):
            cp.pixels[i] = (199, 0, 57)
    elif temp_f > 92:
        for i in range(9):
            cp.pixels[i] = (227, 0, 28)
    else:
        for i in range(10):
            cp.pixels[i] = (255, 0, 0)

    time.sleep(1)
