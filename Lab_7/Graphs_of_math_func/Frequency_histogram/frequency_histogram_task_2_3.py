import matplotlib.pyplot as plt
import numpy as np
import os

def derectory_reader(): # Використовуємо функцію для читання дерикторії з лаб 3
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
    
    with open(selected_path, "r", encoding="utf-8") as file:
        text = file.read() 
        if not text.strip():
            print("Файл порожній!")
            letter_frequency() # повторний виклик функції
        
        text = text.lower() # перетворення тексту в нижній регістр
        letter_count = {} # створення словника для зберігання частоти появи літер
        for char in text:
            if char.isalpha(): # перевірка чи символ є літерою
                if char in letter_count:
                    letter_count[char] += 1 # якщо літера вже є в словнику, збільшуємо її частоту
                else:
                    letter_count[char] = 1 # якщо літери немає в словнику, додаємо її з частотою 1
        top10_letters = sorted(letter_count.items(), # сортування літер за частотою появи 
                               key=lambda x: x[1], 
                               reverse=True)[:10] 
        
    return top10_letters # повернення 10 найбільш частих літер

def sentence_frequency():
    """Функція для обчислення частоти появи окличних, питальних, 
    звичайних та речень з трикрапкою у тексті"""
    
    selected_path = derectory_reader() # вибір файлу
    
    with open(selected_path, "r", encoding="utf-8") as file:
        text = file.read()
        if not text.strip():
            print("Файл порожній!")
            sentence_frequency() # повторний виклик функції
        
        constructs = { 
            ".": ".",
            "!": "!",
            "?": "?",
            "...": "..."
        }
        
        freq_dict = {}
        for name, substring in constructs.items():
            freq_dict[name] = text.count(substring) # підрахунок частоти появи речень
            
        sorted_freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)) # сортування частоти речень
    
    return sorted_freq_dict # повернення частоти речень      

def plot_letter_frequency():
    """Функція для побудови гістограми частоти появи літер у тексті"""
      
    letter_freq = letter_frequency() # отримання частоти появи літер
    letters, frequencies = zip(*letter_freq) # розділення на літери та частоти
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(letters, frequencies, color='red', edgecolor='black', linewidth=1.5) # побудова гістограми
    plt.title("Частота появи літер у тексті", fontsize=16, fontweight='bold') # заголовок
    plt.xlabel("Літери", fontsize=14) # підпис до осі x
    plt.ylabel("Частота", fontsize=14) # підпис до осі y
    plt.xticks(fontsize=14.5)  # розмір шрифту шкали по X
    plt.yticks(fontsize=14.5)  # розмір шрифту шкали по Y
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
    if not sentence_freq or not any(sentence_freq.values()): # перевірка на наявність даних
        print("Немає даних для побудови гістограми речень")      
        return
          
    sentences = list(sentence_freq.keys())
    frequencies = list(sentence_freq.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(sentences, frequencies, color='red', edgecolor='black', linewidth=1.5)
    plt.title("Частота появи речень у тексті", fontsize=14, fontweight='bold') # заголовок
    plt.xlabel("Речення", fontsize=14) # підпис до осі x
    plt.ylabel("Частота", fontsize=14) # підпис до осі y
    plt.xticks(fontsize=14.5)  # розмір шрифту шкали по X
    plt.yticks(fontsize=14.5)  # розмір шрифту шкали по Y
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
    
    print("Програма для побудови гістограм частоти появи літер та речень у тексті")
    
    menu = {
        1: "Гістограма частоти появи літер",
        2: "Гістограма частоти появи речень",
        3: "Вихід"
    }
    
    while True:
        print("\nОберіть дію:")
        for key, value in menu.items():
            print(f"{key}. {value}")
        
        try:
            choice = int(input("Ваш вибір: "))
            if choice == 1:
                plot_letter_frequency() # виклик функції для побудови гістограми частоти появи літер
            elif choice == 2:
                plot_sentence_frequency() # виклик функції для побудови гістограми частоти появи речень
            elif choice == 3:
                print("Вихід з програми")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Введіть правильне число")    
    
if __name__ == "__main__":
    main() # виклик основної функції
           
     
