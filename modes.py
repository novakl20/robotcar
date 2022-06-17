from microbit import button_a, sleep,
from motors import carStop, carDrive
from sensors import fetchSensorData
from LED import lightsON, lightsBreakON, lightsIndicator, indicator_warning
from us import distance
from utime import ticks_us, ticks_diff

def speedR():
    count = 0
    state = fetchSensorData()['SpeedRight']
    start = ticks_us()
    while count != 3:
        if fetchSensorData()['SpeedRight'] != state:
            count += 1
            state = fetchSensorData()['SpeedRight']
    return ticks_diff(ticks_us(), start)
    
def speedL():
    count = 0
    state = fetchSensorData()['SpeedLeft']
    start = ticks_us()
    while count != 3:
        if fetchSensorData()['SpeedLeft'] != state:
            count += 1
            state = fetchSensorData()['SpeedLeft']
    return ticks_diff(ticks_us(), start)

def mode0():
    #fce, kdy auto zastaví, rosvítí brzdová světla a zapne výstražná světla
    carStop()
    lightsBreakON()
    lightsIndicator(indicator_warning)

def mode1():
    #mod, kde auto jede dopředu a reaguje na překážku
    lightsON()
    while fetchSensorData()['ObstclLeft'] == '0' or fetchSensorData()['ObstclRight'] == '0' or distance() < 50:
        mode0()
    carDrive(0, 100, 0, 100)
    print(speedR(), speedL())
    
def mode2():
    #mod, kde auto...
    pass