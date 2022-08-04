# Import the required modules
import microbit
import radio

# Switch on the radio hardware
radio.on()

# Definition of variables for data transfer
data0 = "0"
data1 = "0"
data = "00"

px = 0
py = 0

# Definition of variables for range to value of accelerometer
amin = 200
amax = 1050

# query loop
while True:
    a = microbit.accelerometer.get_values() # read the accelerometer values
    ax = a[0]
    ay = a[1]

# Assign the letters to a direction and store in data0
    if ax >= amin and ay <= -amin: # micro:bit tilted to the left-forward
        data0 = "lf"
    elif ax < amin and ax > -amin and ay <= -amin: # micro:bit tilted to the forward
        data0 = "f"       
    elif ax <= -amin and ay <= -amin: # micro:bit tilted to the right-forward
        data0 = "rf"
    elif ax >= amin and ay >= amin: # micro:bit tilted to the left-backward
        data0 = "lb"
    elif ax < amin and ax > -amin and ay >= amin: # micro:bit tilted to the backward
        data0 = "b"
    elif ax <= -amin and ay >= amin: # micro:bit tilted to the right-backward
        data0 = "rb"    
    else: # else 0
        data0 = "0"

# value ov accelerometer in absolute value
    Absax = abs(ax)
    Absay = abs(ay)

# determine relativ value of range of accelerometer
    if Absax < amin:
        px = 0
    elif Absax > amax:
        px = 1
    else:
        px = (Absax - amin)/(amax-amin)
    
    if Absay < amin:
        py = 0
    elif Absay > amax:
        py = 1
    else:
        py = (Absay - amin)/(amax-amin)

# Assign the letters to a button and store in data1
    if microbit.button_a.is_pressed() == 1 and microbit.button_b.is_pressed() == 0:
        data1 = "a"
    elif microbit.button_a.is_pressed() == 0 and microbit.button_b.is_pressed() == 1:
        data1 = "b"
    elif microbit.button_a.is_pressed() == 1 and microbit.button_b.is_pressed() == 1:
        data1 = "c"
    else:
        data1 = "0"
    
    data = data0 + data1 + px + py # put data0 and data1 together and store in data
    
    radio.send(data) # Send data
    
