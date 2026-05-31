import requests
from bs4 import BeautifulSoup
import json

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    print("Страница загружена!!!")

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    if books:
        first_book = books[0]
        title = first_book.find("h3").find('a')['title']
        price = first_book.find("p", class_='price_color').text

        print(f"Название книги: {title}")
        print(f"Цена книги: {price}")

    books_data = []
    for book in books[:5]:
        books_data.append({
            "title": book.find("h3").find('a')['title'],
            "price": book.find("p", class_='price_color').text,
            'rating': book.find('p', class_='star-rating')['class'][1]
        })

    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books_data, f, ensure_ascii=False, indent = 2)

    print(f"Сохранено {len(books_data)} книг в books.json")
else:
    print(f'Ошибка: {response.status_code}')
