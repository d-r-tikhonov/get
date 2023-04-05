import RPi.GPIO as gpio
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp   = 4
troyka = 17

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binary(value, n):
    return [int (elem) for elem in bin(value)[2:].zfill(n)]

def adc():
    for i in range(256):
        dacValue = decimal2binary(i, 8)
        gpio.output(dac, dacValue)

        compValue = gpio.input(comp)

        sleep(0.1)
        
        if (compValue == 0):
            return i

try:
    while True:
        i = adc()

        if i != 0:
            print(i, '--> {:.2f}V'.format(3.3*i/256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
        


