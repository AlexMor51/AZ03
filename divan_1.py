import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/divany"
driver.get(url)
time.sleep(5)

# Собираем элементы, содержащие цены
price_elements = driver.find_elements("css selector", 'div.q5Uds.T7z9Z.fxA6s > span.ui-LD-ZU.KIkOH[data-testid="price"]')

# Извлекаем текст (цены) из элементов
prices = [price.text for price in price_elements]
# Сохранение данных в CSV
df = pd.DataFrame({'Цена': prices})
df.to_csv("prices_divan.csv", index=False)
print(len(prices))

# Закрываем браузер
driver.quit()