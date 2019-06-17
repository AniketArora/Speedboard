from RPi import GPIO

import time

from Eindopdracht.mcp3008 import Mcp3008

GPIO.setmode(GPIO.BCM)
Mcp = Mcp3008(0, 0)

try:
    while True:
        x = Mcp.read_channel(0)
        y = Mcp.read_channel(1)
        print("X: " + str(x))
        print("Y: " + str(y))
        time.sleep(1)

except KeyboardInterrupt:
    print(" Bye!")

finally:
    GPIO.cleanup()
