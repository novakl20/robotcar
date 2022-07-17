# Import the required modules
import microbit
import radio

# Switch on the radio hardware
radio.on()

# Definition of variables for data transfer
data0 = "0"
data1 = "0"
data = "00"

# query loop
while True:
    a = microbit.accelerometer.get_values() # read the accelerometer values

# Assign the letters to a direction and store in data0
    if a[0] >= 300 and a[1] <= 300: # micro:bit tilted to the left and not forward beyond the threshold
        data0 = "l"
    elif a[0] <= -300 and a[1] <= 300: # micro:bit tilted to the right and not forward beyond the threshold
        data0 = "r"
    elif a[1] <= -300 and a[0] >= -300 and a[0] <= 300: # micro:bit tilted forward and not sideways beyond the threshold
        data0 = "f"
    elif a[1] >= 300: # micro:bit tilted backwards
        data0 = "b"
    else: # else 0
        data0 = "0"

# Assign the letters to a button and store in data1
    if microbit.button_a.is_pressed() == 1 and microbit.button_b.is_pressed() == 0:
        data1 = "a"
    elif microbit.button_a.is_pressed() == 0 and microbit.button_b.is_pressed() == 1:
        data1 = "b"
    elif microbit.button_a.is_pressed() == 1 and microbit.button_b.is_pressed() == 1:
        data1 = "c"
    else:
        data1 = "0"
    data = data0 + data1 # put data0 and data1 together and store in data
    radio.send(data) # Send data