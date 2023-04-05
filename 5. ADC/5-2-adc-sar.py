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
    k = 0
    
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, decimal2binary(k, 8))

        sleep (0.1)

        if gpio.input(comp) == 0:
            k -= 2**i

    return k

try:
    while True:
        k = adc()

        if k != 0:
            print(k, '--> {:.2f}V'.format(3.3*k/256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
        


