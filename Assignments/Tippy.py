from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration  # Get acceleration along X, Y, Z axes

    if x > 6:  # Check if the switch is to the right
        for i in range(5):
            cp.pixels[1] = (0, 1, 0)  # Turn on pixels 1-3
            cp.pixels[2] = (0, 1, 0)
            cp.pixels[3] = (0, 1, 0)
        for i in range(1, 3):
            cp.pixels[1] = (0, 0, 0)  # Turn off pixels 1-3 to green
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
    elif x < 6:  # Switch is to the left
        for i in range(5):
            cp.pixels[6] = (1, 0, 0)  # Turn of pixels 6-8 red
            cp.pixels[7] = (1, 0, 0)
            cp.pixels[8] = (1, 0, 0)
        for i in range(1, 3):
            cp.pixels[6] = (0, 0, 0)  # Turn off pixels
            cp.pixels[7] = (0, 0, 0)
            cp.pixels[8] = (0, 0, 0)
