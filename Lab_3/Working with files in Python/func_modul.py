import os
import csv
 
def new_file(): # 1)Створення нового файлу
    """Функція для створення нового файлу .txt в заданій директорії files/"""  
    
    name_file = input('Введіть назву файлу: ') 
    with open(f'files/{name_file}.csv', 'w+', encoding='utf-8', newline='') as csvfile: # створення файлу
        name_columns = ['   Прізвище Ім\'я', ' Група', ' Середній бал'] # назви колонок
        writer = csv.DictWriter(csvfile, fieldnames=name_columns) # запис колонок у файл
        writer.writeheader() # запис заголовка
        print(f'Файл {name_file} створено') 
        
def derectory_reader(): # 2)Вибір файлу для роботи
    """Функція читає директорію files/ та дає можливість обрати файл для читання
    Файл обирається за номером у списку"""
    
    file_list = os.listdir('files') # список файлів у директорії files/
    file_list = [folder for folder in file_list if os.path.isfile(os.path.join('files', folder)) and folder.endswith('.csv')] # вибірка файлів з розширенням .csv

    if not file_list: # якщо файлів немає
        print("У директорії 'files/' немає файлів.")
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
                selected_path = os.path.join('files', selected_file) # шлях до файлу
                print(f"Вибрано файл: {selected_file}") # вивід вибраного файлу
                return selected_path # повернення шляху до файлу
            else:
                print(f"Введіть число від 1 до {len(file_list)}")
        except ValueError:
            print("Введіть правильне число")

def add_student(): # 3)Додавання студента
    """Функція для додавання студента в файл обраний функцією derectory_reader()
    з можливістю додавання одного або декількох студентів"""
    
    selected_path = derectory_reader() # вибір файлу для додавання студентів
    
    print("\nДодавання студентів:")
    while True:
        student = input("Введіть дані студента у форматі 'Прізвище ім'я, група, середній бал': ")
        
        parts = [part.strip() for part in student.split(',')] # розділення введених даних
        if len(parts) < 3: # перевірка чи введені всі дані
            print("Недостатньо даних. Потрібно: Прізвище, Ім'я, Група, Середній бал")
            continue
        
        # Валідація ПІБ (перевірка на наявність цифр)
        if any(char.isdigit() for char in parts[0]):
            print("Помилка: Прізвище та ім'я не повинні містити цифри")
            continue
        
        # Валідація групи (формат XX-00 або подібний)
        if len(parts) > 1:
            group = parts[1].strip()
            if not (2 <= len(group) <= 6) or not ('-' in group):
                print("Помилка: Група має бути у форматі 'XX-00'")
                continue
                
        with open(selected_path, 'a', encoding='utf-8', newline='') as csvfile: # відкриття файлу для додавання
            writer = csv.writer(csvfile) # запис в файл
            writer.writerow(parts[:3])  # Беремо перші 3 елементи
    
        end = input("Продовжити додавання? (Enter - Так, n - Ні): ")
        if end == '':
            continue
        elif end == 'n':
            print("Додавання студентів завершено")
            break
          
def read_file(): # 4)Читання файлу
    """Функція для читання файлу обраного функцією derectory_reader()"""
    
    selected_path = derectory_reader() # вибір файлу для читання
    
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
        reader = csv.reader(csvfile) # читання файлу
        print("\nДані студентів:")
        for student_num, row in enumerate(reader): # перебір рядків файлу
            if student_num == 0: # пропуск заголовка
                print(f"{row[0]}  {row[1]}  {row[2]}") # вивід заголовка
                print("-" * 40) # розділювач
            else:
                print(f"{student_num}. {row[0]} | {row[1]} | {row[2]}") # вивід даних студентів
    return None

def search_student_name(): # 5)Пошук студента за прізвищем
    """функція для пошуку студента за прізвищем в файлі обраному функцією derectory_reader()
    та вивидення його данних"""
    
    selected_path = derectory_reader() # вибір файлу для пошуку
     
    search = input("Введіть прізвище студента: ")
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
        reader = csv.reader(csvfile) # читання файлу
        for student_num, row in enumerate(reader): # перебір рядків файлу
            if student_num == 0: # пропуск заголовка
                continue
            if search in row[0]: # пошук студента за прізвищем
                print(f"Студент {row[0]} з групи {row[1]} має середній бал {row[2]}") # вивід даних студента                 
                return {
                    'path': selected_path,
                    'student_num': student_num,
                    'name': row[0],
                    'group': row[1],
                    'average': row[2]    
                }                   
            
                    
        #end = input("Продовжити пошук? (Enter - Так, n - Ні): ")
        #if end == '':
        #    continue
        #else:
        #    print("Пошук завершено")
        #    break
                
def search_student_num(): # 6)Пошук студента за номером
    """Функція для пошуку студента за номером в файлі обраному функцією derectory_reader()
    та вивидення його данних"""
    
    selected_path = derectory_reader() # вибір файлу для пошуку
    
    search = int(input("Введіть номер студента: ")) 
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
        reader = csv.reader(csvfile) # читання файлу
        for student_num, row in enumerate(reader): # перебір рядків файлу
            if student_num == 0: # пропуск заголовка
                continue 
            if search == student_num: # пошук студента за номером
                print(f"Студент {row[0]} з групи {row[1]} має середній бал {row[2]}") # вивід даних студента
                return { # повернення даних студента
                'path': selected_path,
                'student_num': student_num,
                'name': row[0],
                'group': row[1],
                'average': row[2]    
                }         
        
def editing_student(): # 7)Редагування студента
    """Функція для редагування всіх даних про студента 
    з можливістю вибору по номеру та призвищу"""
                     
    print("\nВиберіть спосіб пошуку студента:")
    
    menu = { # меню вибору способу пошуку
        1: "Пошук за номером",
        2: "Пошук за прізвищем"
    }     
    for key, value in menu.items(): # вивід меню
        print(f"{key}: {value}") 
        
    choice = int(input("Оберіть спосіб пошуку \nта введіть відповідний номер: "))       
    
    while True:            
        if choice == 1:
            student = search_student_num() # вибір студента за номером
            break
        elif choice == 2:
            student = search_student_name() # вибір студента за прізвищем
            break
        else:
            print("Виберіть відповідний номер")
            choice = int(input("Оберіть спосіб пошуку \nта введіть відповідний номер: "))
            continue
    
    # Перевірка чи знайдено студента
    if not student:
        print("Не вдалося знайти студента")
        return None
    
    current_student = { # дані студента
    'name': student['name'], #
    'group': student['group'],
    'average': student['average']
    }
    print("\nВибраний студент:")
    print(f"Прізвище та ім'я: {current_student['name']}") # вивід даних студента
    print(f"Група: {current_student['group']}")
    print(f"Середній бал: {current_student['average']}")
    
    print("\nРедагування даних студента:")
    new_name = input(f"Прізвище та ім'я ({current_student['name']}): ") or current_student['name'] # введення нових даних
    new_group = input(f"Група ({current_student['group']}): ") or current_student['group']
    new_score = input(f"Середній бал ({current_student['average']}): ") or current_student['average']    
    
    new_student = [new_name, new_group, new_score] # нові дані студента
    
    print("\nНові дані студента:") # вивід нових даних
    print(f"Прізвище та ім'я: {new_name}")
    print(f"Група: {new_group}")
    print(f"Середній бал: {new_score}")
    
    confirm = input("Зберегти зміни? (Enter - Так, n - Ні): ") # підтвердження збереження змін
    if confirm == '':
        with open(student['path'], 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
            reader = csv.reader(csvfile) # читання файлу
            rows = list(reader) # перетворення файлу в список
            rows[student['student_num']] = new_student # заміна даних студента на нові
            
        with open(student['path'], 'w', encoding='utf-8', newline='') as csvfile: # відкриття файлу для запису
            writer = csv.writer(csvfile) # запис в файл
            writer.writerows(rows) # запис рядків у файл
        print("Зміни збережено")
    else:
        print("Зміни не збережено")   
    
def sort_average(): # 8)Сортування студентів за середнім балом
    """Функція для сортування студентів за середнім балом по зростанню та спаданню в файлі обраному функцією derectory_reader()"""
    
    selected_path = derectory_reader() # вибір файлу для сортування
    
    menu = {
        1: "Сортування за середнім балом по зростанню",
        2: "Сортування за середнім балом по спаданню"
    }  
    
    for key, value in menu.items(): # вивід меню
        print(f"{key}: {value}")  
    
    choice = int(input("Оберіть спосіб сортування \nта введіть відповідний номер: "))
    
    if choice == 1:
        with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
            reader = csv.reader(csvfile) # читання файлу
            rows = list(reader) # перетворення файлу в список
            rows = rows[1:] # пропуск заголовка
            rows.sort(key=lambda x: float(x[2])) # сортування студентів за середнім балом по зростанню
            
            print("\nСортування студентів за середнім балом по зростанню:")
            print("Прізвище Ім'я | Група | Середній бал")
            
            for row in rows: # вивід даних студентів
                print(f"{row[0]} | {row[1]} | {row[2]}") # вивід даних студентів
    
    elif choice == 2:
        with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
            reader = csv.reader(csvfile) # читання файлу
            rows = list(reader) # перетворення файлу в список
            rows = rows[1:] # пропуск заголовка
            rows.sort(key=lambda x: float(x[2]), reverse=True) # сортування студентів за середнім балом по спаданню
            
            print("\nСортування студентів за середнім балом по спаданню:")
            print("Прізвище Ім'я | Група | Середній бал")
            
            for row in rows: # вивід даних студентів
                print(f"{row[0]} | {row[1]} | {row[2]}") # вивід даних студентів
    else:
        print("Виберіть відповідний номер")
        choice = int(input("Оберіть спосіб сортування \nта введіть відповідний номер: "))

def remove_student(): # 9)Видалення студента
    """Функція для видалення студента з файлу обраного функцією derectory_reader()"""
    
    selected_path = derectory_reader()
    
    search = input("Введіть прізвище студента: ")
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile: # відкриття файлу для читання
        reader = csv.reader(csvfile) # читання файлу
        rows = list(reader) # перетворення файлу в список
        for student_num, row in enumerate(rows): # перебір рядків файлу
            if student_num == 0: # пропуск заголовка
                continue
            if search in row[0]: # пошук студента за прізвищем
                print(f"Студент {row[0]} видалений") # вивід повідомлення про видалення
                rows.pop(student_num) # видалення студента
                break
        else:
            print("Студент не знайдений")
            return None
        
    with open(selected_path, 'w', encoding='utf-8', newline='') as csvfile: # відкриття файлу для запису 
        writer = csv.writer(csvfile) # запис в файл
        writer.writerows(rows) # запис рядків у файл  
    
    
    


    
       
    

    
    
    