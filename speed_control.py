# Import of the micro:bit module
from microbit import *
from sensors import fetchSensorData
from time import *
from math import pi

speed_left = fetchSensorData()['SpeedLeft']
speed_right = fetchSensorData()['SpeedRight']

def speedRight():
    state = fetchSensorData()['SpeedRight']
    start = ticks_us()
    while True:
        if state != fetchSensorData()['SpeedRight']:
            end = ticks_us()
            break
        continue
    diff_right = ticks_diff(end,start)
    w_r = (100000*pi)/diff_right
    print('R ', w_r)

def speedLeft():
    state = fetchSensorData()['SpeedLeft']
    start = ticks_us()
    while True:
        if state != fetchSensorData()['SpeedLeft']:
            end = ticks_us()
            break
        continue
    diff_left = ticks_diff(end,start)
    w_l = (100000*pi)/diff_left
    print('L ', w_l)

'''
while True:
    speedRight()
    speedLeft()
    '''