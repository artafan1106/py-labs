import numpy
import time
import matplotlib.pyplot as plt
from buble_sort import bubble_sort
from quick_sort import quick_sort
from insert_sort import insertion_sort
from shell_sort import shell_sort

metod = int(input('Введите номер метода сортировки (buble sort - 1), (quick sort - 2), (insertion - 3), (shell sort - 4): '))

result_time = [] # ----- массив для записи времени выполнения сортировки
n = 1000 # ----- начальное кол-во элементов
x = n # ----- шаг по кол-ву элементов

if metod == 1:
    for i in range(10):
        oldlist = numpy.random.randint(0, 100, n)
        start = time.time()
        newlist = bubble_sort(oldlist)
        end = time.time()
        n += x
        result_time.append(end-start)
        print(len(newlist))

if metod == 2:
    for i in range(10):
        oldlist = numpy.random.randint(0, 100, n)
        start = time.time()
        newlist = quick_sort(oldlist)
        end = time.time()
        n += x
        result_time.append(end-start)
        print(len(newlist))

if metod == 3:
    for i in range(10):
        oldlist = numpy.random.randint(0, 100, n)
        start = time.time()
        newlist = insertion_sort(oldlist)
        end = time.time()
        n += x
        result_time.append(end-start)
        print(len(newlist))

if metod == 4:
    for i in range(10):
        oldlist = numpy.random.randint(0, 100, n)
        start = time.time()
        newlist = shell_sort(oldlist)
        end = time.time()
        n += x
        result_time.append(end-start)
        print(len(newlist))

fig, ax = plt.subplots()

ax.plot(numpy.arange(1000, 10000+1, 1000), result_time, label='Time')
ax.legend()

plt.title('Зависимость роста времени сортировки от размера входного массива')
plt.xlabel('Кол-во элементов в массиве')
plt.ylabel('Время выполнения')
plt.show()
