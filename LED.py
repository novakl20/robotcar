from microbit import pin0, sleep
from neopixel import NeoPixel

#definování konstant a barev
np = NeoPixel(pin0, 8)
headlights = (0, 3)
backlights = (5, 6)
led_white = (60, 60, 60)
led_red = (60, 0, 0)
led_off = (0, 0, 0)
led_red_br = (255, 0, 0)
led_orange = (100, 35, 0)
indicator_left = (1, 4)
indicator_right = (2, 7)
indicator_warning = (1, 2, 4, 7)

def carON():
    for x in range(20):
        for a in range(0, 8):
            np[a] = led_orange
        np.show()
        sleep(120-(x*5))
        np.clear()
        sleep(120-(x*5))

def lightsON():
    for x in headlights:
        np[x] = led_white
    for x in backlights:
        np[x] = led_red
    np.show()

def lightsOFF():
    for x in headlights:
        np[x] = led_off
    for x in backlights:
        np[x] = led_off
    np.show()

def lightsBreakON():
    for x in backlights:
        np[x] = led_red_br
    np.show()

def lightsBreakOFF():
    pass

def lightsIndicator(direction):
    for x in direction:
        np[x] = led_orange
    np.show()
    sleep(200)
    for x in direction:
        np[x] = led_off
    np.show()
    sleep(200)
        
"""
#testování všech funkcí světel
while True:
    lightsON()
    sleep(2000)
    lightsBreakON()
    sleep(2000)    
    lightsOFF()
    sleep(2000)
    lightsIndicator(indicator_left)
    lightsIndicator(indicator_right)
    lightsIndicator(indicator_warning)
"""