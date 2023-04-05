import RPi.GPIO as gpio
from time import sleep

dac  = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 15, 12, 7, 8, 25, 24]

comp   = 4
troyka = 17

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binary(value, n):
    return [int (elem) for elem in bin(value)[2:].zfill(n)]

def sar_adc():
    k = 0
    
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, decimal2binary(k, 8))

        sleep (0.005)

        if gpio.input(comp) == 0:
            k -= 2**i

    return k

def flash_adc():
    for i in range(256):
        dacValue = decimal2binary(i, 8)
        gpio.output(dac, dacValue)

        compValue = gpio.input(comp)

        sleep(0.005)
        
        if (compValue == 0):
            return i

def volume(n):
    n = int(10*n/256)
    mas = [0] * 8

    for i in range(n - 1):
        mas[i] = 1

    return mas

try:
    while True:
        value = sar_adc()

        if value != 0:
            gpio.output(leds, volume(value))
            print(value, '--> {:.2f}V'.format(3.3*value/256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
        


