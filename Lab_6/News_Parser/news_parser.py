import requests as req
from bs4 import BeautifulSoup as bs
import sqlite3 as sql

# Функція для отримання HTML-коду сторінки
def get_html_url(url): 
    """Отримує URL сторінки та повертає HTML-код для подальшого парсингу"""
    try:
        link = req.get(url)
        if link.status_code == 200:
            return link.text
        else:
            print(f"Error: {link.status_code}")
            return None
    except ValueError:
        print(f"Невірний URL: {url}")
        return None

# Функція для парсингу HTML-коду            
def parse_html(html): 
    """Парсить HTML-код та підраховує частоту слів,
    HTML-тегів, кількість посилань та зображень"""
    
    soup = bs(html, 'lxml')
    
    text = soup.get_text(strip=True)  # Отримання тексту з HTML-коду
     
    symbols = "!@#$%^&*()_+-`~[]{};:|↑—=|\'\",.·<>?/"
    for s in symbols: # Очищення тексту від непотрібних символів та знаків пунктуації
        text = text.replace(s, ' ')  
        
    words = text.split() # Розділення тексту на слова
    word_count = {} # Словник для підрахунку частоти слів
    for word in words: # Підрахунок частоти слів
        word = word.lower()
        if word not in word_count: 
            word_count[word] = 1 
        else:
            word_count[word] += 1
    
    tag_count = {} # Словник для підрахунку частоти HTML-тегів
    for tag in soup.find_all(True): # Підрахунок частоти HTML-тегів
        tag_name = tag.name
        if tag_name not in tag_count:
            tag_count[tag_name] = 1
        else:
            tag_count[tag_name] += 1
    
    links = len(soup.find_all('a')) # Підрахунок кількості посилань
    images = len(soup.find_all('img')) # Підрахунок кількості зображень
    
    return word_count, tag_count, links, images # Повертаємо результати парсингу

# Функція для збереження результатів у базу даних
def save_to_db(word_count, tag_count, links, images): 
    conn = sql.connect('data_news_parser.db') # Підключення до бази даних
    cursor = conn.cursor() # Створення курсора для виконання SQL-запитів
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS word_count (word TEXT PRIMARY KEY, count INTEGER)''') # Створення таблиці для частоти слів
    cursor.execute('''CREATE TABLE IF NOT EXISTS tag_count (tag TEXT PRIMARY KEY, count INTEGER)''') # Створення таблиці для частоти HTML-тегів
    cursor.execute('''CREATE TABLE IF NOT EXISTS links_images (links INTEGER, images INTEGER)''') # Створення таблиці для кількості посилань та зображень
    
    for word, count in word_count.items(): # Збереження частоти слів
        cursor.execute('INSERT OR REPLACE INTO word_count (word, count) VALUES (?, ?)', (word, count))
    
    for tag, count in tag_count.items(): # Збереження частоти HTML-тегів
        cursor.execute('INSERT OR REPLACE INTO tag_count (tag, count) VALUES (?, ?)', (tag, count))
    
    cursor.execute('INSERT OR REPLACE INTO links_images (links, images) VALUES (?, ?)', (links, images)) # Збереження кількості посилань та зображень
    
    conn.commit() # Застосування змін до бази даних
    conn.close() # Закриття з'єднання з базою даних

# Функція для відображення результатів парсингу    
def display_results(word_count, tag_count, links, images):
    print("Частота слів:")
    for word, count in word_count.items(): # Виведення частоти слів
        print(f"{word}: {count}")
    
    print("\nЧастота HTML-тегів:")
    for tag, count in tag_count.items(): # Виведення частоти HTML-тегів
        print(f"{tag}: {count}")
    
    print(f"\nКількість посилань: {links}") # Виведення кількості посилань
    print(f"Кількість зображень: {images}") # Виведення кількості зображень

def main():
    while True:
        url = input("Введіть URL сторінки новин: ") 
        html = get_html_url(url) # Отримання HTML-коду сторінки
        if html:
            break
        else:
            print("Спробуйте ще раз")
    
    word_count, tag_count, links, images = parse_html(html) # Парсинг HTML-коду
    save_to_db(word_count, tag_count, links, images) # Збереження результатів у базі даних
    display_results(word_count, tag_count, links, images) # Відображення результатів парсингу
        
if __name__ == "__main__":
    main()
