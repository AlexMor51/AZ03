import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(125)
y = np.random.rand(125)

plt.scatter(x, y)
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("Случайные числа по оси x")
plt.ylabel("Случайные числа по оси y")

plt.show()