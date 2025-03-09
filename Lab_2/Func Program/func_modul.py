import random as r
import datetime as dt

def ask_mans(n): # Function 1
    """Функція, яка приймає номер місяця і виводить пору року"""
    if n == 12 or n == 1 or n == 2: # 12, 1, 2 - зима
        print("Пора року: Зима")
    elif 3 <= n <= 5: # 3, 4, 5 - весна
        print("Пора року: Весна")
    elif 6 <= n <= 8: # 6, 7, 8 - літо
        print("Пора року: Літо")
    elif 9 <= n <= 11: # 9, 10, 11 - осінь
        print("Пора року: Осінь")
    else:
        print("Такого місяця не існує") # якщо введено невірне значення
        
def ask_year(year): # Function 2
    """Функція яка приймає рік і виводить True якщо він високосний та Folse якщо ні"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # перевірка чи рік високосний
        return True # якщо високосний
    else:
        return False # якщо не високосний

def date_correct(day, month, year): # Function 3
    """Функція яка перевіряє правильність введення дати"""
    
    if year <= 0: # перевірка року
        return False
    
    if month < 1 or month > 12: # перевірка місяця
        return False
    
    days_in_month = { # кількість днів у місяці                
        1: 31,  # Січень
        2: 29 if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else 28,  # Лютий
        3: 31,  # Березень
        4: 30,  # Квітень
        5: 31,  # Травень
        6: 30,  # Червень
        7: 31,  # Липень
        8: 31,  # Серпень
        9: 30,  # Вересень
        10: 31, # Жовтень
        11: 30, # Листопад
        12: 31  # Грудень
    }
    
    if day < 1 or day > days_in_month[month]: # перевірка дня
        return False
        
    return True

def search_date(dates): # Function 4
    """Функція яка отримує список дат у форматі dd.mm.yyyy та
    та шукає у ньому повтори дат та виводить їх список
    Parameters:
    dates (list): Список дат у форматі dd.mm.yyyy
    
    Returns:
    list: Список повторюваних дат або повідомлення про їх відсутність"""
    
    date_counts = {} # створюємо словник для підрахунку дат
    
    for date in dates: # перебір дат
        # Перевіряємо формат дати
        parts = date.split('.') # розділяємо дату на частини
        if len(parts) != 3: # якщо дата не має трьох частин
            print(f"Неправильний формат дати: {date}") # виводимо повідомлення
            continue
        
        # Розбиваємо дату на день, місяць та рік
        day, month, year = map(int, parts)
    
        if date_correct(day, month, year):
            # Якщо дата існує, додаємо її до словника
            if date in date_counts:
                date_counts[date] += 1
            else:
                date_counts[date] = 1
        else:
            print(f"Дата {date} не існує") # виводимо повідомлення
        
    duplicates = {date: count for date, count in date_counts.items() if count > 1} # знаходимо дати з лічильником більше 1
    return duplicates if duplicates else {"Немає однакових дат"} # повертаємо словник дублікатів або повідомлення про їх відсутність
    
def random_data(): # Function 5
    """Функція у якої немає аргументів та яка повертає випадкову дату у форматі "dd.mm.yyyy" """
    while True: # цикл для введення дат
        day = r.randint(1, 31) # випадковий день
        month = r.randint(1, 12) # випадковий місяць
        year = r.randint(1939, 2077) # випадковий рік
        
        if month == 2:
            if ask_year(year):
                if day <= 29:
                    break
            else:
                if day <= 28:
                    break
        elif month in [4, 6, 9, 11]:
            if day <= 30:
                break
        else:
            break
    return f"{day:02d}.{month:02d}.{year}" # виведення випадкової дати

def dates(date1, date2): # Function 6
    """Функція яка отримує дві дати в форматі dd.mm.yyyy та
    виводить різницю в днях між ними. З використанням бібліотеки datetime та її функцією datetime"""
    
    date1 = dt.datetime.strptime(date1, "%d.%m.%Y") # перетворюємо стрічку в об'єкт datetime
    date2 = dt.datetime.strptime(date2, "%d.%m.%Y") # перетворюємо стрічку в об'єкт datetime
    
    difference = date1 - date2 # знаходимо різницю між датами
    days = difference.days # знаходимо кількість днів
    years = days // 365  # знаходимо кількість років
    
    return days, years # повертаємо кількість днів та років

def ask_month (nam_month): # Function 7
    """Функція яка приймає як аргумент номер місяця і виводить його нзву\n
    на екран та нічого не повертає.
    
    Parameters:
    month_number (int): Номер місяця (1-12)
    """
    month = { # словник з назвами місяців
         1: "Січень",
         2: "Лютий",
         3: "Березень", 
         4: "Квітень", 
         5: "Травень",
         6: "Червень", 
         7: "Липень",
         8: "Серпень",
         9: "Вересень",
         10: "Жовтень",
         11: "Листопад",
         12: "Грудень"
    } 
    
    if not isinstance(nam_month, int) or nam_month < 1 or nam_month > 12: # перевірка чи введено число та чи воно в межах від 1 до 12
        print("Такого місяця не існує")
    else:
        print(month[nam_month]) # виведення назви місяця
        
   