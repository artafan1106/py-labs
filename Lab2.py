import math
import matplotlib.pyplot as plt
import numpy as np
from Lab1 import *

fig, ax = plt.subplots()

n_start = int(1)
n_stop = int(200)
n_step = int(1)

rect_integral_data = []
tr_integral_data = []
simpsons_integral_data = []

ideal_value = 8/3

for n_current in range(n_start, n_stop+n_step, n_step):
    print(f"n_current = {n_current}")
    rect_integral_data.append(math.fabs(ideal_value - rect_integral(fn, lower_limit, upper_limit, n_current)))
    tr_integral_data.append(math.fabs(ideal_value - tr_integral(fn, lower_limit, upper_limit, n_current)))
    simpsons_integral_data.append(math.fabs(ideal_value - simpsons_(lower_limit, upper_limit, n_current)))

ax.plot(rect_integral_data, label='rect')
ax.plot(tr_integral_data, label='tr')
ax.plot(simpsons_integral_data, label='simpsons')
ax.legend()


plt.show()