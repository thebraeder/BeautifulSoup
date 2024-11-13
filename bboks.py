import requests
from bs4 import BeautifulSoup
import csv

# Базовый URL сайта
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Создаем и открываем CSV-файл для записи с правильными разделителями
with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
    # Используем разделитель ";" для лучшего отображения в Excel
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Записываем заголовки столбцов
    writer.writerow(['Title', 'Price', 'Availability'])

    # Цикл по всем страницам (от 1 до 50)
    for page in range(1, 51):
        # Формируем URL для текущей страницы
        url = base_url.format(page)

        # Отправляем запрос на сайт
        response =   

        # Проверяем статус запроса
        if response.status_code == 200:
            # Парсим HTML-код страницы с помощью BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Находим все элементы книги на странице
            books = soup.find_all('article', class_='product_pod')

            # Проходим по каждой книге и извлекаем данные
            for book in books:
                # Извлекаем название книги
                title = book.h3.a['title']

                # Извлекаем цену книги
                price = book.find('p', class_='price_color').text

                # Извлекаем статус наличия
                availability = book.find('p', class_='instock availability').text.strip()

                # Записываем данные в CSV-файл
                writer.writerow([title, price, availability])

            print(f"Страница {page} успешно обработана.")
        else:
            print(f"Не удалось получить страницу {page}. Статус: {response.status_code}")

print("Сбор данных завершен, данные сохранены в 'books.csv'")
