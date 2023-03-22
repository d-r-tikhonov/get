import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

dac = [26,19,13,6,5,11,9,10]
gpio.setup(dac, gpio.OUT, initial = gpio.HIGH)

pwm = gpio.PWM(14,1000)
pwm.start(0)

try:
    while True:
        dutyCicle = int(input())
        pwm.ChangeDutyCycle(dutyCicle)
        print ("{:.2f}".format(dutyCicle*3.3/100))

finally:
    gpio.output(2,0)
    gpio.output(dac, 0)
    gpio.cleanup()