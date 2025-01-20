from parser import get_page_content, parse_books
from bs4 import BeautifulSoup

# URL страницы с классической литературой
url = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"

def main():
    try:
        # Получаем HTML-контент страницы
        page_content = get_page_content(url)

        # Парсим страницу с помощью BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')

        # Извлекаем информацию о книгах
        books = parse_books(soup)

        # Выводим информацию о книгах
        for book in books:
            print(f"Название: {book['title']}")
            print(f"Цена: {book['price']}")
            print('-' * 50)

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
