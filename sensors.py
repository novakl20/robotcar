# Import of the micro:bit module
from microbit import *

# Initialization of the I2C interface
i2c.init(freq = 400000, sda = pin20, scl = pin19)

# Since the zfill function is not included in micro:bit Micropython, it must be inserted as a function
def zfill(s, width):
    return '{:0>{w}}'.format(s, w=width)

# Read out IO Expander data and store in sen_data
def fetchSensorData():
    data = "{0:b}".format(ord(i2c.read(0x38, 1))) # Read hexadecimal data and convert to binary
    data = zfill(data, 8)  # fill up the data to 8 digits if necessary
    bol_data_dict = {}  # declare bol_data_dict as dictionary
    bit_count = 7  # Counter for the loop that enters the data from data into bol_data_dict
    # Transfer data from data in bol_data_dict
    bol_data_dict = {
        'SpeedLeft': data[7],
        'SpeedRight': data[6],
        'LineTrackerLeft': data[5],
        'LineTrackerMiddle': data[4],
        'LineTrackerRight': data[3],
        'ObstclLeft': data[2],
        'ObstclRight': data[1],
        'Buzzer': data[0]
        }
        
    return bol_data_dict  # bit 0 = SpeedLeft, bit 1 = SpeedRight, bit 2 = LineTrackerLeft, bit 3 = LineTrackerMiddle, bit 4 = LineTrackerRight, bit 5 = ObstclLeft, bit 6 = ObstclRight, bit 7 = Buzzer

'''
# while loop executes and displays the showSensorData with an interval of one second
while True:
    print("Načtená data:")
    print(fetchSensorData())
    sleep(1000)
'''