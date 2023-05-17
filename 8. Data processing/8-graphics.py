from matplotlib import pyplot
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker

#считываем данные из файлов
with open('/home/b01-206/get/8. Data processing/settings.txt') as settings_file:
    settings = [float(i) for i in settings_file.read().split('\n')]

data = np.loadtxt('/home/b01-206/get/8. Data processing/data.txt', dtype = int) * settings[1]
data_time = np.array([i * settings[0] for i in range(data.size)])

#параметры фигуры
fig, ax = pyplot.subplots(figsize = (16, 10), dpi = 500)

#устанавливаем минимальные и максимальные значения для осей
ax.set(xlim = (data_time.min(), data_time.max()), ylim = (data.min(), data.max()))

#устанавливаем интервал основных делений
# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#название графика
ax.set_title("\n".join(wrap('Процесс зарядки и разрядки конденсатора в RC-цепи', 60)), loc = 'center')

#сетка основная и второстепенная
ax.grid(which = 'major', color = 'k')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'gray', linestyle = ':')

#подпись осей
ax.set_ylabel("Напряжение U, В")
ax.set_xlabel("Время t, с")

#линия с легендой
ax.plot(data_time, data, c = 'black', linewidth = 1, label = 'U(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'blue', s = 10)
ax.legend(shadow = False, loc = 'right', fontsize = 30)

#сохранение графика
fig.savefig('/home/b01-206/get/8. Data processing/graph.png')
fig.savefig('/home/b01-206/get/8. Data processing/graph.svg')


