from microbit import pin2, sleep

# Variables needed for conversion
uref = 0.00322265625 # 3,3 V / 1024 (max. voltage at ADC-Pin / ADC Resolution)
uratio = 2.7857142 # (10 kOhm + 5,6 kOhm) / 5,6 kOhm [(R1 + R2) / R2, Voltage divider ratio]

def supplyVoltage():
    adcvoltage = pin2.read_analog() # Reading the ADC value
    voltaged = uref * adcvoltage # Convert ADC value to Volt
    voltagep = voltaged * uratio # Multiply the measured voltage by the voltage divider ratio to calculate the actual voltage
    return voltagep # returns the variable voltagep

# Demo-Loop
while True:
    sup_volt = supplyVoltage() # executes the function supplyVoltage and stores the return value in sup_volt
    print("Input voltage = " + str(sup_volt) + " V") # Outputs the value from sup_volt formatted with text
    sleep(2000)