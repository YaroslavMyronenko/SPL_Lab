def date_correct(day, month, year):
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

      
day = int(input("Введіть день: ")) # введення дня
month = int(input("Введіть місяць: ")) # введення місяця
year = int(input("Введіть рік: ")) # введення року

if date_correct(day, month, year): # виклик функції
    print(f"{day}.{month}.{year} - коректна дата") # виведення результату
else:
    print(f"{day}.{month}.{year} - некоректна дата") # виведення результату