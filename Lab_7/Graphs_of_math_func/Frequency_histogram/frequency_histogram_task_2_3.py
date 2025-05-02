import matplotlib.pyplot as plt
import numpy as np
import os

def derectory_reader(): # Функція для читання дерикторії з лаб 3
    """Функція читає директорію text/ та дає можливість обрати файл для читання
    Файл обирається за номером у списку"""
    
    file_list = os.listdir('Graphs_of_math_func/Frequency_histogram/text/') # список файлів у директорії text/
    file_list = [folder for folder in file_list if os.path.isfile(os.path.join('Graphs_of_math_func/Frequency_histogram/text/', folder)) and folder.endswith('.txt')] # вибірка файлів з розширенням .txt

    if not file_list: # якщо файлів немає
        print("У директорії 'text/' немає файлів.")
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
                selected_path = os.path.join('Graphs_of_math_func/Frequency_histogram/text/', selected_file) # шлях до файлу
                print(f"Вибрано файл: {selected_file}") # вивід вибраного файлу
                return selected_path # повернення шляху до файлу
            else:
                print(f"Введіть число від 1 до {len(file_list)}")
        except ValueError:
            print("Введіть правильне число")

def letter_frequency():
    """Функція для обчислення частоти появи літер у тексті"""
    
    selected_path = derectory_reader() # вибір файлу
    
    if not selected_path:
        print("Помилка Файл не вибрано")
        return 0
    
    with open(selected_path, "r", encoding="utf-8") as file:
        text = file.read()
        text = text.lower() # перетворення тексту в нижній регістр
            
        leter_list = {} # створення словника для зберігання частоти появи літер
        for char in text:
            if char.isalpha(): # перевірка чи символ є літерою
                leter_list[char] = leter_list.get(char, 0) + 1 # додавання літери до словника

        top_list_letter = sorted(leter_list.items(), key=lambda x: x[1], reverse=True)[:10] # сортування літер за частотою появи
    return top_list_letter # повернення списку літер

def sentence_frequency():
    """Функція для обчислення частоти появи окличних, питальних, 
    звичайних та речень з трикрапкою у тексті"""
    
    selected_path = derectory_reader() # вибір файлу
    
    with open(selected_path, "r", encoding="utf-8") as file:
        text = file.read()
        
        if not text.strip():
            print("Попередження Файл порожній")
            return []
    
        text = text.lower() # перетворення тексту в нижній регістр
        
        sentence_list = {} # створення словника для зберігання частоти появи речень
        for char in text:
            if char == "...":
                sentence_list["..."] = sentence_list.get("...", 0) + 1 # додавання речення до словника
            elif char == "?":
                sentence_list["?"] = sentence_list.get("?", 0) + 1 # додавання речення до словника
            elif char == "!":
                sentence_list["!"] = sentence_list.get("!", 0) + 1 # додавання речення до словника
            elif char == ".":
                sentence_list["."] = sentence_list.get(".", 0) + 1 # додавання речення до словника

    top_list_sentence = sorted(sentence_list.items(), key=lambda x: x[1], reverse=True)[:10] # сортування речень за частотою появи
    return top_list_sentence

def plot_letter_frequency():
    """Функція для побудови гістограми частоти появи літер у тексті"""
      
    letter_freq = letter_frequency() # отримання частоти появи літер
    if not letter_freq:
        print("Немає даних для побудови гістограми літер")
        return 0
    
    letters, frequencies = zip(*letter_freq) # розділення на літери та частоти
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(letters, frequencies, color='red', edgecolor='black', linewidth=1.5) # побудова гістограми
    plt.title("Частота появи літер у тексті", fontsize=16, fontweight='bold') # заголовок
    plt.xlabel("Літери", fontsize=14) # підпис до осі x
    plt.ylabel("Частота", fontsize=14) # підпис до осі y
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    max_height = max(frequencies)
    plt.ylim(0, max_height * 1.15)
    
    for bar in bars:
        y_num = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y_num + max_height * 0.03, int(y_num), 
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    plt.tight_layout() # автоматичне підлаштування розмірів графіку
    plt.savefig("Graphs_of_math_func/Graphs_png/letter_frequency_task_2.png") # збереження графіку у файл
    plt.show() # показ графіку
 
def plot_sentence_frequency():
    """Функція для побудови гістограми частоти появи речень у тексті"""
    
    sentence_freq = sentence_frequency() # отримання частоти появи речень
    if not sentence_freq:
        print("Немає даних для побудови гістограми речень")
        return 0
    
    sentences, frequencies = zip(*sentence_freq) # розділення на речення та частоти
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(sentences, frequencies, color='red', edgecolor='black', linewidth=1.5)
    plt.title("Частота появи речень у тексті", fontsize=14, fontweight='bold') # заголовок
    plt.xlabel("Речення", fontsize=14) # підпис до осі x
    plt.ylabel("Частота", fontsize=14) # підпис до осі y
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    max_height = max(frequencies)
    plt.ylim(0, max_height * 1.15)
    
    for bar in bars:
        y_num = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y_num + max_height * 0.03, int(y_num),
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    plt.tight_layout() # автоматичне підлаштування розмірів графіку
    plt.savefig("Graphs_of_math_func/Graphs_png/sentence_frequency_task_3.png") # збереження графіку у файл
    plt.show() # показ графіку    
    

def main():
    """Основна функція для виклику інших функцій"""
    plot_letter_frequency() # виклик функції для побудови гістограми частоти появи літер
    plot_sentence_frequency() # виклик функції для побудови гістограми частоти появи речень
   
if __name__ == "__main__":
    main() # виклик основної функції
           
     
