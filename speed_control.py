# Import of the micro:bit module
from microbit import display
from sensors import fetchSensorData
from utime import ticks_ms, ticks_diff, ticks_add, sleep

# Values for counting the speed of the wheels
period = 3 # time for evalueting the speed
deadline = 0 # time interval for counting the speed
countL = 0 # number of "ticks" on the left wheel sensor
countR = 0 # number of "ticks" on the right wheel sensor
stateL = fetchSensorData()['SpeedLeft']
stateR = fetchSensorData()['SpeedRight']
data_to_send = []

def speed():
    global deadline, countL, countR, stateL, stateR
    
    if ticks_diff(deadline, ticks_ms()) > 0:
        if stateL != fetchSensorData()['SpeedLeft']:
            countL += 0.5
            stateL = fetchSensorData()['SpeedLeft']
        if stateR != fetchSensorData()['SpeedRight']:
            countR += 0.5
            stateR = fetchSensorData()['SpeedRight']
        return None
    else:
        data_to_send = [countL, countR]
        deadline = ticks_add(ticks_ms(), int(period * 1000))
        countL = 0
        countR = 0
        return data_to_send