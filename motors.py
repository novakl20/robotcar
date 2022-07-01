# Import of the micro:bit module
from microbit import i2c, pin19, pin20

# Initialisierung der I2C Schnittstelle
i2c.init(freq = 400000, sda = pin20, scl = pin19)

# Initialisierung des PWM Controllers
i2c.write(0x70, b'\x00\x01')
i2c.write(0x70, b'\xE8\xAA')

# Durch die Verzögerung eines Motors kann eine durch produktionsbedingte Toleranzen unterschiedliche Drehzahl der Motoren ausgeglichen werden.
biasR = 0 # Verzögerung des rechten Motors in Prozent
biasL = 8 # Verzögerung des linken Motors in Prozent

# Die scale Funktion wird genutzt um die bias-Variablen für die Berechnung der Motorgeschwindigkeit umzuskalieren.
def scale(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Motoren mithilfe des PWM Controllers steuern
# PWM0 und PWM1 für den linken und PWM2 und PWM3 für den rechten Motor
def carDrive(PWM0, PWM1, PWM2, PWM3):
    PWM0 = int(PWM0 * (scale(biasR, 0, 100, 100, 0) / 100)) # Skalierung des Verzögerungswerts in den Wert in Prozent mit dem der Motor drehen soll. Bsp: bias = 5 wird in 95 umgewandelt und anschliessend durch 100 geteilt. 255 * (95/100).
    PWM1 = int(PWM1 * (scale(biasR, 0, 100, 100, 0) / 100)) # Wiederholen des Vorgangs für alle 4 Kanäle
    PWM2 = int(PWM2 * (scale(biasL, 0, 100, 100, 0) / 100))
    PWM3 = int(PWM3 * (scale(biasL, 0, 100, 100, 0) / 100))
    i2c.write(0x70, b'\x02' + bytes([PWM0])) # Wert für PWM Kanal (0-255) an PWM Controller übertragen. 0x70 ist die I2C Adresse des Controllers. b'\x02 ist das Byte für den PWM Kanal 1. Zu dem Byte für den Kanal wird das Byte mit dem PWM Wert zu addiert.
    i2c.write(0x70, b'\x03' + bytes([PWM1])) # Wiederholen des Vorgangs für alle 4 Kanäle
    i2c.write(0x70, b'\x04' + bytes([PWM2]))
    i2c.write(0x70, b'\x05' + bytes([PWM3]))

# stop all motors
def carStop():
    carDrive(0, 0, 0, 0)