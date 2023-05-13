# Написати програму для конвертації .csv файлу у .json і навпаки.
#
# Перший студент має створити .csv файл, у який програмно записати кілька рядків.
# Програмно реалізувати переписування даних із .csv у .json файл.
# У програмному коді реалізувати обробку виключних ситуацій по роботі з файлами.
#
# Другий студент повинен написати програмний код, який переписує дані з .json файла,
# написаного попереднім студентом, у .csv файл,
# при йому  додавши у файл кілька нових рядків.
# Третій студент переписує вміст .csv файлу у .json файл, додаючи нові рядки, і т.д.
# У програмному коді коментарі обов'язкові.

import csv
import json

csv_path_books = r'docs/books.csv'
json_path_books = r'docs/books.json'


# функція для конвертації CSV файлу у JSON
def make_json(csv_file_path, json_file_path):
    # створюємо словник для даних
    data = {}

    try:
        # відкриваємо CSV файл
        with open(csv_file_path, encoding='utf-8') as csvf:
            reader = csv.DictReader(csvf)

            # зчитуємо дані з CSV файлу і записуємо їх у словник
            for rows in reader:
                # використовуємо title як ключ
                key = rows['title']
                data[key] = rows
    except FileNotFoundError as e:
        # обробляємо помилки
        print(f"File {e.filename} cannot be opened.")

    # відкриваємо json і записуємо дані зі словника
    try:
        with open(json_file_path, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
    except FileNotFoundError as e:
        # обробляємо помилки
        print(f"File {e.filename} cannot be created.")


def task7():
    # KarinaChernobai start

    try:
        # створюємо файл
        with open('docs/books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # створюємо дані
            fields = ["author", "title", "genre"]
            rows = [
                ["Jane Austen", "Emma", "romance"],
                ["Sylvia Plath", "Ariel", "poetry"],
                ["Sylvia Plath", "The Bell Jar", "autobiorgaphy"],
                ["Sarah Waters", "Fingersmith", "romance"],
                ["Charlotte Bronte", "Jane Eyre", "romance"],
                ["Mary Shelley", "Frankenstein", "horror"],
            ]
            # записуємо дані
            writer.writerow(fields)
            writer.writerows(rows)
    except FileNotFoundError as e:
        # обробляємо помилки
        print(f"File {e.filename} cannot be created.")

    # викликаємо функцію конвертації файлу
    make_json(csv_path_books, json_path_books)

    # KarinaChernobai end
    return
