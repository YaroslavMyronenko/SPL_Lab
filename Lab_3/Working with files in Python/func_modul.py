import os
import csv
import sys

def new_file():
    """Функція для створення нового файлу .txt в заданій директорії files/"""  
    
    name_file = input('Введіть назву файлу: ')
    with open(f'files/{name_file}.csv', 'w+', encoding='utf-8', newline='') as csvfile:
        name_columns = ['   Прізвище Ім\'я', ' Група', ' Середній бал']
        writer = csv.DictWriter(csvfile, fieldnames=name_columns)
        writer.writeheader()
        print(f'Файл {name_file} створено')
        
def derectory_reader():
    """Функція читає директорію files/ та дає можливість обрати файл для читання
    Файл обирається за номером у списку"""
    
    file_list = os.listdir('files')
    file_list = [folder for folder in file_list if os.path.isfile(os.path.join('files', folder)) and folder.endswith('.csv')]

    if not file_list:
        print("У директорії 'files/' немає файлів.")
        return None
    
    print("\nСписок доступних файлів:")
    for namber, file in enumerate(file_list, 1):
        print(f"{namber}. {file}")
    
    while True:
        try:
            choice = int(input("\nВведіть номер файлу для вибору: "))
            if 1 <= choice <= len(file_list):
                selected_file = file_list[choice - 1]
                selected_path = os.path.join('files', selected_file)
                print(f"Вибрано файл: {selected_file}")
                return selected_path
            else:
                print(f"Введіть число від 1 до {len(file_list)}")
        except ValueError:
            print("Введіть правильне число")

def add_student():
    """Функція для додавання студента в файл обраний функцією derectory_reader()
    з можливістю додавання одного або декількох студентів"""
    
    selected_path = derectory_reader()
    
    print("Для завершення додавання студентів натисніть Enter без введення даних")
    while True:
        student = input("Введіть дані студента у форматі 'Прізвище ім'я, група, середній бал': ")
        
        parts = [part.strip() for part in student.split(',')]
        if len(parts) < 3:
            print("Недостатньо даних. Потрібно: Прізвище, Ім'я, Група, Середній бал")
            continue
                
        with open(selected_path, 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(parts[:3])  # Беремо перші 3 елементи
    
        end = input("Продовжити додавання? (Enter - Так, n - Ні): ")
        if end == '':
            continue
        else:
            print("Додавання студентів завершено")
            break
          
def read_file():
    """Функція для читання файлу обраного функцією derectory_reader()"""
    
    selected_path = derectory_reader()
    
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        print("\nДані студентів:")
        for student_num, row in enumerate(reader):
            if student_num == 0:
                print(f"{row[0]}  {row[1]}  {row[2]}")
                print("-" * 40)
            else:
                print(f"{student_num}. {row[0]} | {row[1]} | {row[2]}")
    return None

def search_student_name():
    """функція для пошуку студента за прізвищем в файлі обраному функцією derectory_reader()
    та вивидення його данних"""
    
    selected_path = derectory_reader()
    
    search = input("Введіть прізвище студента: ")
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for student_num, row in enumerate(reader):
            if student_num == 0:
                continue
            if search in row[0]:
                print(f"Студент {row[0]} з групи {row[1]} має середній бал {row[2]}")                 
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
                
def search_student_num():
    """Функція для пошуку студента за номером в файлі обраному функцією derectory_reader()
    та вивидення його данних"""
    
    selected_path = derectory_reader()
    
    search = int(input("Введіть номер студента: "))
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for student_num, row in enumerate(reader):
            if student_num == 0:
                continue
            if search == student_num:
                print(f"Студент {row[0]} з групи {row[1]} має середній бал {row[2]}")
                return {
                'path': selected_path,
                'student_num': student_num,
                'name': row[0],
                'group': row[1],
                'average': row[2]    
                }         
        
def editing_student():
    """Функція для редагування всіх даних про студента 
    з можливістю вибору по номеру та призвищу"""
                     
    print("\nВиберіть спосіб пошуку студента:")
    
    menu = {
        1: "Пошук за номером",
        2: "Пошук за прізвищем"
    }     
    for key, value in menu.items():
        print(f"{key}: {value}")
        
    choice = int(input("Оберіть спосіб пошуку \nта введіть відповідний номер: "))       
    
    while True:            
        if choice == 1:
            student = search_student_num()
            break
        elif choice == 2:
            student = search_student_name()
            break
        else:
            print("Виберіть відповідний номер")
            choice = int(input("Оберіть спосіб пошуку \nта введіть відповідний номер: "))
            continue
    
    current_student = {
    'name': student['name'],
    'group': student['group'],
    'average': student['average']
    }
    print("\nВибраний студент:")
    print(f"Прізвище та ім'я: {current_student['name']}")
    print(f"Група: {current_student['group']}")
    print(f"Середній бал: {current_student['average']}")
    
    print("\nРедагування даних студента:")
    new_name = input(f"Прізвище та ім'я ({current_student['name']}): ") or current_student['name']
    new_group = input(f"Група ({current_student['group']}): ") or current_student['group']
    new_score = input(f"Середній бал ({current_student['average']}): ") or current_student['average']    
    
    new_student = [new_name, new_group, new_score]
    
    print("\nНові дані студента:")
    print(f"Прізвище та ім'я: {new_name}")
    print(f"Група: {new_group}")
    print(f"Середній бал: {new_score}")
    
    confirm = input("Зберегти зміни? (Enter - Так, n - Ні): ")
    if confirm == '':
        with open(student['path'], 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            rows[student['student_num']] = new_student
            
        with open(student['path'], 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        print("Зміни збережено")
    else:
        print("Зміни не збережено")   
    
def remove_student():
    """Функція для видалення студента з файлу обраного функцією derectory_reader()"""
    
    selected_path = derectory_reader()
    
    search = input("Введіть прізвище студента: ")
    with open(selected_path, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for student_num, row in enumerate(rows):
            if student_num == 0:
                continue
            if search in row[0]:
                print(f"Студент {row[0]} видалений")
                rows.pop(student_num)
                break
        else:
            print("Студент не знайдений")
            return None
        
    with open(selected_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    

#new_file()
#add_student()
#read_file()
#search_student_name()
#search_student_num()
#editing_student()
#remove_student()         
    
    
    
    


    
       
    

    
    
    