import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12 ,7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

dac = [26, 19, 13 ,6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)

comp = 4
troyka = 17

gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def adc():
    k = 0
    
    for i in range(7,-1,-1):
        k += 2**i
        gpio.output(dac, decimal2binary(k, 8))
        time.sleep(0.001)

        if gpio.input(comp) == 0:
            k -= 2**i

    return k

def decimal2binary(value, n):
    return [int (elem) for elem in bin(value)[2:].zfill(n)]

try:
    voltage = 0
    measure = []
    time_start = time.time()
    count = 0

    ############################################################################################################################################################################
    #                                           Измерения зависимости напряжения на конденсаторе от времени
    ############################################################################################################################################################################

    print('Начало зарядки конденсатора')
    while voltage < 256 * 0.80:
        voltage = adc()
        measure.append(voltage)
        count += 1
        gpio.output(leds, decimal2binary(voltage, 8))
    
    gpio.setup(troyka, gpio.OUT, initial=gpio.LOW)

    print('Начало разрядки конденсатора')
    while voltage > 256*0.02:
        voltage = adc()
        measure.append(voltage)
        count += 1
        gpio.output(leds, decimal2binary(voltage, 8))

    time_experiment = time.time() - time_start

    ############################################################################################################################################################################
    #                                           Запись данных в файл
    ############################################################################################################################################################################

    print('Запись данных в файл')

    with open('/home/b01-206/get/7. Measure/data.txt', 'w') as dataFile:
        for i in measure:
            dataFile.write(str(i) + '\n')
    
    with open ('/home/b01-206/get/7. Measure/settings.txt', 'w') as settingsFile:
        settingsFile.write('Частота дискретизации: ' + str(count/time_experiment) + '\n')
        settingsFile.write('Шаг квантования АЦП: 0.01289')

    print('Общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/time_experiment/count, 0.013))

    ############################################################################################################################################################################
    #                                           Построение графика
    ############################################################################################################################################################################

    print ('Построение графика')
    y = [i/256*3.3 for i in measure]
    x = [i*time_experiment/count for i in range(len(measure))]

    pyplot.plot(x,y)

    pyplot.xlabel('Время t, с')
    pyplot.ylabel('Напряжение U, В')

    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()