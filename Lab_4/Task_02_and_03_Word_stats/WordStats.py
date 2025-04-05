import os

def derectory_reader(): # Вибір файлу для роботи
    """Функція читає директорію та дає можливість обрати файл для читання
    Файл обирається за номером у списку"""
    
    path_project = os.path.dirname(os.path.abspath(__file__)) # шлях до директорії проекту
    all_files = os.listdir(path_project) # список всіх файлів у директорії проекту
    
    file_list = [file for file in all_files if os.path.isfile(os.path.join(path_project, file)) and file.endswith('.txt')] # вибірка файлів з розширенням .csv

    if not file_list: # якщо файлів немає
        print("У директорії немає файлів.")
        return None
    
    print("Оберіть файл для роботи:"
          "\nСписок доступних файлів:")
    for namber, file in enumerate(file_list, 1): # вивід списку файлів
        print(f"{namber}. {file}") # вивід файлів
    
    while True:
        try: 
            choice = int(input("\nВведіть номер файлу для вибору: ")) 
            if 1 <= choice <= len(file_list): # перевірка чи введене число в діапазоні
                selected_file = file_list[choice - 1] # вибір файлу
                selected_path = os.path.join(path_project, selected_file) # шлях до файлу
                print(f"Вибрано файл: {selected_file}") # вивід вибраного файлу
                return selected_path # повернення шляху до файлу
            else:
                print(f"Введіть число від 1 до {len(file_list)}")
        except ValueError:
            print("Введіть правильне число")

def text_reader(file_path):
    """Функція для читання текстового файлу"""
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def text_statistics(text):
    """Функція для визначення загальної кількості символів з пробілами і без, 
    кількості всих слів та унікальних слів у тексті"""  
     
    chars_with_spaces = len(text) # Загальна кількість символів у тексті з пробілами 
    
    chars_without_spaces = len(text.replace(" ", "")) # Загальна кількість символів у тексті без пробілів
    
    words = text.split()  # Розбиваємо текст на слова, використовуючи пробіл як роздільник
    words = [word.strip('.,!?;:"()_-—') for word in words]  # Видаляємо розділові знаки з кожного слова  
    total_words = len(words) # Загальна кількість слів у тексті
    
    unique_words = set(words)
    total_unique_words = len(unique_words) # Загальна кількість різних слів (без повторів)
    
    unique_word_count = sum(1 for word in unique_words if words.count(word) == 1) # Кількість унікальних слів, що зустрічаються тільки один раз
    
    return {
        "total_chars_with_spaces": chars_with_spaces,
        "total_chars_without_spaces": chars_without_spaces,
        "total_words": total_words,
        "total_unique_words": total_unique_words,
        "unique_word_count": unique_word_count
    }
    
def text_length_statistics(text):
    """Функція для визначення максимальної, мінімальної та середньої
    довжини слів, речень та абзаців у тексті"""

    words = text.split()  # Розбиваємо текст на слова, використовуючи пробіл як роздільник
    words = [word.strip('.,!?;:"()_-—') for word in words if word.strip('.,!?;:"()_-—')]  # Видаляємо розділові знаки з кожного слова
    sentences = text.split('. ')  # Розбиваємо текст на речення, використовуючи крапку як роздільник
    sentences = [sentence.strip() for sentence in sentences if sentence]  # Видаляємо пусті речення
    paragraphs = text.split('\n')  # Розбиваємо текст на абзаци, використовуючи новий рядок як роздільник     
    paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph]  # Видаляємо пусті абзаци
    
    # Довжина слів
    word_lengths = [len(word) for word in words]  # Довжина кожного слова
    max_word_length = max(word_lengths) if word_lengths else 0  # Максимальна довжина слова
    min_word_length = min(word_lengths) if word_lengths else 0  # Мінімальна довжина слова
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0  # Середня довжина слова
    
    # Довжина речень
    sentence_lengths = [len(sentence.split()) for sentence in sentences]  # Довжина кожного речення
    max_sentence_length = max(sentence_lengths) if sentence_lengths else 0  # Максимальна довжина речення
    min_sentence_length = min(sentence_lengths) if sentence_lengths else 0  # Мінімальна довжина речення
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0  # Середня довжина речення
    
    # Довжина абзаців
    paragraph_lengths = [len(paragraph.split()) for paragraph in paragraphs]  # Довжина кожного абзацу
    max_paragraph_length = max(paragraph_lengths) if paragraph_lengths else 0  # Максимальна довжина абзацу
    min_paragraph_length = min(paragraph_lengths) if paragraph_lengths else 0  # Мінімальна довжина абзацу
    avg_paragraph_length = sum(paragraph_lengths) / len(paragraph_lengths) if paragraph_lengths else 0  # Середня довжина абзацу
     
    return {
        "max_word_length": max_word_length,
        "min_word_length": min_word_length,
        "avg_word_length": avg_word_length,
        "max_sentence_length": max_sentence_length,
        "min_sentence_length": min_sentence_length,
        "avg_sentence_length": avg_sentence_length,
        "max_paragraph_length": max_paragraph_length,
        "min_paragraph_length": min_paragraph_length,
        "avg_paragraph_length": avg_paragraph_length
    }


main_menu = { # Список головного меню
        1: "Статистика тексту",
        2: "Інформація про довжину слів, реченнь та абзаців",
        3: "Вихід"
    }

while True: 
    for key, value in main_menu.items():
        print(f"{key}: {value}")
        
    menu = (input("\nОберіть функцію: "))
        
    # Валідація введення
    if not menu.isdigit(): # перевірка чи введене число
        print("Номер повинен бути числом від 1 до 3"
            "Продовжити роботу з програмою? (Введіть n для завершення або Enter для продовження)")
        if input() == "n":
            print("До побачення!")
            break
        else:
            continue 
    
    menu = int(menu) # перетворення введеного значення в число
        
    # Валідація введення
    if menu not in main_menu:
        print("Не вірний номер функції виберіть від 1 до 3"
            "Продовжити роботу з програмою? (Введіть n для завершення або Enter для продовження)")
        if input() == "n":
            print("До побачення!")
            break
        else:
            continue 
            
    # Виклики функцій
    if menu == 1: 
        print("===================================")
        file_path = derectory_reader()  # Виклик функції для вибору файлу
        text = text_reader(file_path)  # Читаємо текст з файлу
        statistics = text_statistics(text)  # Отримуємо інформацію тексту

        print("\nЗагальна кількість символів у тексті з пробілами:", statistics["total_chars_with_spaces"])
        print("Загальна кількість символів у тексті без пробілів:", statistics["total_chars_without_spaces"])
        print("\nЗагальна кількість слів у тексті:", statistics["total_words"])
        print("Загальна кількість різних слів у тексті:", statistics["total_unique_words"])
        print("Кількість унікальних слів, що зустрічаються тільки один раз:", statistics["unique_word_count"])    
        
        # Запит на продовження роботи з програмою
        print("Продовжити роботу з програмою? (Введіть n для завершення або Enter для продовження)")
        if input() == "n":
            print("До побачення!")
            break
        else:
            continue
        
    elif menu == 2:
        print("===================================")
        file_path = derectory_reader()  # Виклик функції для вибору файлу
        text = text_reader(file_path)  # Читаємо текст з файлу
        statistics = text_length_statistics(text)  # Отримуємо інформацію про довжину слів, речень та абзаців
        
        print("\nМаксимальна довжина слова:", statistics["max_word_length"])
        print("Мінімальна довжина слова:", statistics["min_word_length"])
        print("Середня довжина слова:", statistics["avg_word_length"])
        print("\nМаксимальна довжина речення:", statistics["max_sentence_length"])
        print("Мінімальна довжина речення:", statistics["min_sentence_length"])
        print("Середня довжина речення:", statistics["avg_sentence_length"])
        print("\nМаксимальна довжина абзацу:", statistics["max_paragraph_length"])
        print("Мінімальна довжина абзацу:", statistics["min_paragraph_length"])
        print("Середня довжина абзацу:", statistics["avg_paragraph_length"])
        
        # Запит на продовження роботи з програмою
        print("Продовжити роботу з програмою? (Введіть n для завершення або Enter для продовження)")
        if input() == "n":
            print("До побачення!")
            break
        else:
            continue
            
    elif menu == 3:
        print("Вихід з програми")
        break
    
    break



