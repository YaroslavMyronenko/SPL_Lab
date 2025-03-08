def date(dates):
    """Функція яка отримує список дат у форматі dd.mm.yyyy та
    та шукає у ньому повтори дат та виводить їх список"""
    
    date_counts = {} # створюємо словник для підрахунку дат
    
    for date in dates: # перебираємо список дат
        if date in date_counts: # якщо дата вже є в словнику
            date_counts[date] += 1 # збільшуємо лічильник
        else:
            date_counts[date] = 1 # додаємо дату в словник з лічильником 1
            
    duplicates = [date for date, count in date_counts.items() if count > 1] # знаходимо дати з лічильником більше 1
    return duplicates if duplicates else ["Немає однакових дат"] # повертаємо список дублікатів або повідомлення про їх відсутність        

dates = [] # створюємо пустий список для дат

while True: # цикл для введення дат
    date_inupt = input("Введіть дати у форматі dd.mm.yyyy (натисніть Enter\nз пустим полем для завершення): ") # введення дат
    
    if date_inupt == "": # якщо натиснуто Enter
        break # вихід з циклу
    
    dates.append(date_inupt) # додавання дати в список

print(f"\nДати що повторюються: {date(dates)}") # виклик функції