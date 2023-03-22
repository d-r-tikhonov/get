import RPi.GPIO as gpio
import sys

dac = [26,19,13,6,5,11,9,10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def decimal2binary(value, n):
    return [int (elem) for elem in bin(value)[2:].zfill(n)]

try:
    while(True):
        value = input('input 0-255: ')
        if (value == 'q'):
            sys.exit()
        elif value.isdigit() and int(value) % 1 == 0 and 0 <= int(value) <=255:
            gpio.output(dac, decimal2binary(int(value), 8))
            print("{:.4f}".format(int(value)/256*3.3))
        elif not value.isdigit():
            print('input number 0-255: ')

except ValueError:
    print('input number 0-255: ')

except KeyboardInterrupt:
    print('done')

finally:
    gpio.output(dac, 0)
    gpio.cleanup()