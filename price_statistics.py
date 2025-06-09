import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

# Загрузка данных из CSV-файла
file_path = 'clean_prices.csv'
data = pd.read_csv(file_path)
df=DataFrame(data)
mean_price = df['Цена'].mean()

# столбец с ценами называется 'Цена'
prices = data['Цена']
# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')
# Мы можем изменить количество bin-ов по своему усмотрению

# Добавление заголовка и меток осей
plt.title(f"Гистограмма цен\nСредняя цена дивана - {round(mean_price)} руб.")
plt.xlabel('Цена')
plt.ylabel('Частота')
# Показать гистограмму
plt.show()