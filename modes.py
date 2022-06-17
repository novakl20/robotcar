from microbit import button_a, sleep, pin16
from motors import carStop, carDrive
from sensors import fetchSensorData
from LED import lightsON, lightsBreakON, lightsIndicator, indicator_warning
from us import distance
from utime import ticks_us, ticks_diff
import radio
import music

# Switch on the radio hardware
radio.on()

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
    incoming = radio.receive() # Reception via radio hardware is stored in the incoming variable
    if incoming != None: # if incoming is not None (empty) then:
        lightsON()
        if incoming[0] == "l": # Query for the 1st character for the direction
            carDrive(120, 0, 0, 120)
        elif incoming[0] == "r":
            carDrive(0, 120, 120, 0)
        elif incoming[0] == "f":
            carDrive(0, 255, 0, 255)
        elif incoming[0] == "b":
            carDrive(150, 0, 150, 0)
        else:
            carStop()
            lightsBreakON()

        if incoming[0] == "b": # turn on and off the reverse light
            pass
        else:
            pass
        
        if incoming[1] == "a": # Query for the 2nd character for the functions (light and horn)
            music.play("c4:1", pin=pin16)
        elif incoming[1] == "b":
            lightsON()
        elif incoming[1] == "c":
            lightsON()
        else:
            pass
        
    else: # if incoming = None, then the Joy-Car is parked.
        # This usually happens when the Joy-Car is out of range of the remote control or when the remote control is off.
        mode0()

