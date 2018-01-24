import time
import board
import neopixel

LEDs = neopixel.NeoPixel(board.NEOPIXEL, 10, bpp=3, brightness=0.3, auto_write=False)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    #else:
    pos -= 170
    return (0, int(pos*3), int(255 - pos*3))

def rainbow(delay):
    for j in range(255):
        for i in range(LEDs.n):
            idx = int((i * 256 / len(LEDs)) + j)
            LEDs[i] = wheel(idx & 255)
        LEDs.show()
        time.sleep(delay)

while True:
    LEDs.fill((255, 0, 0))
    LEDs.show()
    time.sleep(1)

    LEDs.fill((0, 255, 0))
    LEDs.show()
    time.sleep(1)

    LEDs.fill((0, 0, 255))
    LEDs.show()
    time.sleep(1)

    rainbow(0.001) 