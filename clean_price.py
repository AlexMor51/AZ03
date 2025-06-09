import csv

# Имя исходного CSV файла
input_file = "prices_divan.csv"
# Имя выходного CSV файла
output_file = "clean_prices.csv"

# Открываем исходный файл для чтения
with open(input_file, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    # Получаем заголовки
    fieldnames = reader.fieldnames

    # Открываем новый файл для записи
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Записываем заголовок
        writer.writeheader()

        # Обрабатываем строки
        for row in reader:
            # Убираем "руб." из значения столбца `Цена`
            row["Цена"] = row["Цена"].replace("руб.", "").replace(" ", "").strip()
            # Записываем очищенную строку в файл
            writer.writerow(row)

print(f"Данные успешно обработаны и сохранены в файл {output_file}.")