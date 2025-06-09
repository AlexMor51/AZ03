import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=100)
plt.title("Гистограмма случайных чисел,\n распределенных по нормальному распределению")
plt.xlabel("Случайные числа")
plt.ylabel("Частота случайных чисел")

plt.show()