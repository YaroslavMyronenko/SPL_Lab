import datetime as dt

def dates(date1, date2):
    """Функція яка отримує дві дати в форматі dd.mm.yyyy та
    виводить різницю в днях між ними. З використанням бібліотеки datetime та її функцією datetime"""
    
    date1 = dt.datetime.strptime(date1, "%d.%m.%Y") # перетворюємо стрічку в об'єкт datetime
    date2 = dt.datetime.strptime(date2, "%d.%m.%Y") # перетворюємо стрічку в об'єкт datetime
    
    difference = date1 - date2 # знаходимо різницю між датами
    days = difference.days # знаходимо кількість днів
    years = days // 365  # знаходимо кількість років
    
    return days, years # повертаємо кількість днів та років

date1 = str(input("Введіть першу(більшу) дату у форматі dd.mm.yyyy: ")) # введення першої дати
date2 = str(input("Введіть другу(меншу) дату у форматі dd.mm.yyyy: ")) # введення другої дати       

days, years = dates(date1, date2) # виклик функції
if days >= 0: # перевірка чи друга дата менша за першу
    print(f"Різниця між датами: {date1} та {date2} : {days} днів та {years} років") # виведення результату
else:
    print("Перша дата повинна бути меншою за другу") # виведення результату

