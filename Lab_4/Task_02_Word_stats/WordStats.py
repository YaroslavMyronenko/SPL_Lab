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
    """Функція для визначення загальної кількості символів з пробілами і без, слів та унікальних слів у тексті"""  
     
    chars_with_spaces = len(text) # Загальна кількість символів у тексті з пробілами 
    
    chars_without_spaces = len(text.replace(" ", "")) # Загальна кількість символів у тексті без пробілів
    
    words = text.split()  # Розбиваємо текст на слова, використовуючи пробіл як роздільник
    #words = [word.strip('.,!?;:"()[]{}') for word in words]  # Видаляємо розділові знаки з кожного слова  
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


print("===================================")
print("Оберіть файл для роботи з текстом:")
print("Список доступних файлів: \n")
file_path = derectory_reader()  # Виклик функції для вибору файлу
text = text_reader(file_path)  # Читаємо текст з файлу
statistics = text_statistics(text)  # Отримуємо інформацію тексту

print("\nЗагальна кількість символів у тексті з пробілами:", statistics["total_chars_with_spaces"])
print("Загальна кількість символів у тексті без пробілів:", statistics["total_chars_without_spaces"])
print("\nЗагальна кількість слів у тексті:", statistics["total_words"])
print("Загальна кількість різних слів у тексті:", statistics["total_unique_words"])
print("Кількість унікальних слів, що зустрічаються тільки один раз:", statistics["unique_word_count"])


