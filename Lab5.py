import random
import math
import matplotlib.pyplot as plt
import numpy as np

a = 1.0
k = 0.0
f = 1
i = []

while f > 0.0001: #проверка на разницу
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0) #расчёт сколько точек попали в окружность
    f = (math.fabs(math.pi - (4 * k / a))) #считаем разницу
    print (4 * k / a) #умножение на 4(полный круг) и деление на общее кол-во точек
    a += 1 #прибавляем к точке
    i.append(math.fabs(4 * k / a))
                              

print (math.pi) #ввод pi из библиотеки питона

fig, ax = plt.subplots()

plt.xlabel('Кол-во попыток')
plt.ylabel('Значение')
plt.title('График зависимости точности расчета значения интеграла в зависимости от числа испытаний')
                            
ax.plot(i, label='Pi')
ax.legend()

plt.show()
