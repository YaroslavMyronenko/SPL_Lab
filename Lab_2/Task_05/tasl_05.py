import random as r

def random_data():
    """Функція у якої немає аргументів та яка повертає випадкову дату у форматі "dd.mm.yyyy" """
    return f"{r.randint(1, 31):02d}.{r.randint(1, 12):02d}.{r.randint(1939, 2077)}" # виведення випадкової дати

while True: # цикл для введення дат
    data = str(input("Нажміть Enter для виведення випадкової дати: "))
    if data == "": # якщо натиснуто Enter
        print(random_data()) # виклик функції
            
    print("Для завершення програми напишіть в консоль 'exit'") 
    if data == "exit": # якщо введено "exit"
        print("Вихід з програми") 
        break # вихід з циклу
    

    
