from microbit import sleep, button_a, button_b, display
from microbit import Image
from LED import carON
from modes import mode0, mode1, mode2

mode = 0

sleep(500)
display.show(Image.ALL_CLOCKS, loop=False, delay=100)
carON()

while True:
    display.show(mode)
    if button_b.was_pressed() == 1:
        mode = 0
    if button_a.was_pressed() == 1:
        mode += 1
        if mode > 2:
            mode = 0
    
    if mode == 0:
        mode0()
        
    elif mode == 1:
        mode1()
        
    elif mode == 2:
        mode2()