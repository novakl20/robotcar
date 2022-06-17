# Import der benötigten Module
from microbit import *
import gc

DISTANCE_CM_PER_BIT = 0.21 # Distanz in cm pro Bit (Auflösung)

# Initialisierung der SPI-Schnittstelle (Pin12 als Echo-Empfänger)
spi.init(baudrate=50000,bits=8,mode=0,miso=pin12)

# Definition der Funktion distance, die die Entfernungsmessung durchführt
def distance():
    gc.disable() # Garbage Collector deaktivieren
    pin8.write_digital(True) # kurzen Impuls auf dem Trigger Pin des Sensors senden
    pin8.write_digital(False) # Impuls auf dem Trigger Pin beenden
    x = spi.read(200) # 200 Bytes auf Pin 12 lesen und in x ablegen
    high_bits = 0 # high_bits auf 0 setzen

    # Zählung der High Bits
    for i in range(len(x)):
        if x[i] == 0 and high_bits > 0:
            break
        elif x[i] == 0xff:
            high_bits += 8
        else:
            high_bits += bin(x[i]).count('1')
    x = None # leeren der Variablen x
    gc.enable() # Garbage Collector aktivieren
    gc.collect() # aufräumen
    return high_bits * DISTANCE_CM_PER_BIT # Berechnung der Distanz und Rückgabe des errechneten Werts

'''
while True:
    print(str(distance())) # Ausführen und ausgeben der distance Funktion
    sleep(200)
'''