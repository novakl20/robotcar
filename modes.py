from microbit import button_a, sleep, pin16
from motors import carStop, carDrive
from speed_control import speed
from sensors import fetchSensorData
from LED import lightsON, lightsBreakON, lightsIndicator, indicator_warning
from us import distance
from utime import ticks_us, ticks_diff
import radio
import music
import speech

# Switch on the radio hardware
radio.on()

def obstacle():
    return fetchSensorData()['ObstclLeft'] == '0' or fetchSensorData()['ObstclRight'] == '0' or distance() < 30

def collision():
    pass
    #return speed()[0] < 5 or speed()[1] < 5

def obstacle_mode1():
    carStop()
    sleep(300)
    speech.say("Obstacle detected",  speed=92, pitch=60, throat=190, mouth=190)
    sleep(1000)
    for i in range(5):
        mode0()

def collision_mode1():
    carStop()
    sleep(300)
    speech.say("Collision detected",  speed=92, pitch=60, throat=190, mouth=190)
    sleep(1000)

def mode0():
    #fce, kdy auto zastaví, rosvítí brzdová světla a zapne výstražná světla
    carStop()
    lightsBreakON()
    lightsIndicator(indicator_warning)

speedL = 150
speedR = 150

def mode1():
    #mod, kde auto jede dopředu a reaguje na překážku
    global speedL, speedR
    
    lightsON()
    
    if obstacle():
        obstacle_mode1()
        carDrive(0, 150, 150, 0)
        sleep(1000)

    carDrive(0, speedR, 0, speedL)
'''
    speed_value = speed()
    
    if speed_value != None:
        print(speed_value)
        # Uprava pravého PWMka na základě otáček:
        print("Old: PWM L: {}, PWM R: {}".format(speedL, speedR))

        if speed_value[1] < speed_value[0]:
            speedR += 5
        elif speed_value[1] > speed_value[0]:
            speedR -= 5
        else:
            pass
        
        print("NEW: PWM L: {}, PWM R: {}".format(speedL, speedR))
        '''
    
incoming_stored = 'b'

def mode2():
    '''
    Mode for following the black line
    Following signals from sensors are used:
    'LineTrackerLeft'
    'LineTrackerMiddle'
    'LineTrackerRight'
    '''

    #control via remote
    global incoming_stored
    
    incoming = radio.receive()[1]
    if incoming == 'a':
        incoming_stored = incoming
    elif incoming == 'b':
        incoming_stored = incoming

    if incoming_stored == "a": # Query for the 2nd character for the functions (light and horn)
        #obstacle detection and evaluation
        if obstacle():
            obstacle_mode1()

        #line follow logic
        if fetchSensorData()['LineTrackerMiddle'] == '1':
            #it means, car follows the line
            carDrive(0, 150, 0, 150)
        elif fetchSensorData()['LineTrackerLeft'] == '1':
            #it means, car deviates to right --> car must turn left
            carDrive(0, 100, 0, 200) #slower left motor, faster right motor
        elif fetchSensorData()['LineTrackerRight'] == '1':
            #it means, car deviates to left --> car must turn right
            carDrive(0, 200, 0, 100) #slower right motor, faster left motor
    elif incoming_stored == "b":
        mode0()

def mode3():
    incoming = radio.receive() # Reception via radio hardware is stored in the incoming variable
    if incoming != None: # if incoming is not None (empty) then:
        lightsON()
        
        if obstacle():
            music.play(music.RINGTONE)
            lightsIndicator(indicator_warning)
        
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