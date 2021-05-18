import random
import numpy
import time
import matplotlib.pyplot as plt

result_time = []

for n in range (2, 11):
    start = time.time()
    myA = []
    myB = []
    for i in range(n):
        myB.append(random.randint(-100, 100))
        myA.append([])
        for j in range(n):
            myA[i].append(random.randint(-100, 100))
    myB = numpy.array(myB)
    myA = numpy.array(myA)
    otvet = numpy.linalg.solve(myA, myB)
    print(otvet)
    end = time.time()
    result_time.append(round(end - start, 5))
    for i in range(n):
        print(myA[i])
    print(myB)
print (result_time)

fig, ax = plt.subplots()
plt.xlabel('Кол-во попыток')
plt.ylabel('Значение')

ax.plot(result_time,label='time')
ax.legend()
plt.show()

