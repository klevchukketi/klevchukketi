import requests
from bs4 import BeautifulSoup


def get_page_content(url):
    """Загружает содержимое страницы по указанному URL."""
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Не удалось загрузить страницу. Статус код: {response.status_code}")


def parse_books(soup):
    """Извлекает название книг и цену из распарсенной HTML-страницы."""
    books = []

    # Находим все элементы, содержащие информацию о книгах
    product_pods = soup.find_all('article', class_='product_pod')

    for book in product_pods:
        # Название книги
        title = book.find('h3').find('a')['title']

        # Цена книги
        price = book.find('p', class_='price_color').text.strip()

        # Убираем ненужный символ 'Â'
        price = price.replace('Â', '')

        # Добавляем книгу в список
        books.append({'title': title, 'price': price})

    return books
