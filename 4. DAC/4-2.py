import RPi.GPIO as gpio
from time import sleep

dac = [26,19,13,6,5,11,9,10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def decimal2binary(value,n):
    return [int(elem) for elem in bin(value)[2:].zfill(n)]

try:
    while True:
        T = input()

        if not T.isdigit():
            print ('Enter a number, please: ')
        
        t = (int(T)/256)/2

        for i in range(256):
            gpio.output(dac, decimal2binary(i, 8))
            sleep(t)
        for i in range(255, -1, -1):
            gpio.output(dac, decimal2binary(i, 8))
            sleep(t)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()