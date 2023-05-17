from matplotlib import pyplot
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker

#считываем данные из файлов
with open('/home/b01-206/get/8. Data processing/settings.txt') as settings_file:
    settings = [float(i) for i in settings_file.read().split('\n')]

data = np.loadtxt('/home/b01-206/get/8. Data processing/data.txt', dtype = int) * settings[1]
data_time = np.array([i/settings[0] for i in range(data.size)])

#параметры фигуры
fig, ax = pyplot.subplots(figsize = (16, 10), dpi = 500)

#устанавливаем минимальные и максимальные значения для осей
ax.set(xlim = (data_time.min(), data_time.max()), ylim = (data.min(), data.max()))

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
ax.plot(data_time, data, c = 'cadetblue', linewidth = 2, label = 'График зависимости U(t)', marker = '^', markerfacecolor = 'cyan', markeredgecolor = 'black', markersize = 8, markevery = 75)
ax.legend(shadow = False, loc = 'right', fontsize = 14)

#время разрядки и зарядки на графике
ax.text(50.1, 2.25, "Время зарядки = 22.11 с \n" + "Время разрядки = 45.28 с ", fontsize = 14)

#сохранение графика
fig.savefig('/home/b01-206/get/8. Data processing/graph.svg')


