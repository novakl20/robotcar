from microbit import sleep, button_a, button_b, display
from microbit import Image
from LED import carON
from modes import mode0, mode1, mode2, mode3

mode = 0

#TODO
#zde definovat globalni proměné rychlosti RF(RightFront), RR(RightRear), LF, LR
#ty se budou předavat volaným modum, napr. mode1(RF, RR, LF, LR)
#v modulu motors bude zakomponovaná fce počítadlo / rychlost motoru, které bude vyhodnocovat, který motor přibrzdí


sleep(500)
display.show(Image.ALL_CLOCKS, loop=False, delay=100)
carON()

while True:
    display.show(mode)
    if button_b.was_pressed() == 1:
        mode = 0
    if button_a.was_pressed() == 1:
        mode += 1
        if mode > 3:
            mode = 0
    
    if mode == 0:
        mode0()
        
    elif mode == 1:
        mode1()
        
    elif mode == 2:
        mode2()
    
    elif mode == 3:
        mode3()