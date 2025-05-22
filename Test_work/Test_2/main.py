import func

def main():
    
    menu = {
        1: "Написати пісню",
        2: "Кількість щасливих квитків",
        3: "Вийти з програми"
    }

    while True:
        for key, value in menu.items():
            print(f"{key}: {value}")
            
        choise = input("\nОберіть функцію: ")
        if not choise.isdigit():
            print("\nНомер повинен бути числом від 1 до 3")
            continue
        
        choise = int(choise)
        if choise not in menu:
            print("\nНе вірний номер функції виберіть від 1 до 3")
            continue
        
        if choise == 1:
            print("\nВведіть числа для написання пісні")
            x = int(input("Введіть число x: "))
            y = int(input("Введіть число y: "))
            z = int(input("Введіть число z (0 або 1): "))
            if z not in [0, 1]:
                print("\nНевірне число z виберіть 0 або 1")
                continue
            print("\n", func.song(x, y, z))
            
        elif choise == 2:
            print("\nВведіть числа для перевірки щасливих квитків")
            num_1 = int(input("Введіть число 1: "))
            num_2 = int(input("Введіть число 2: "))
            if num_1 > num_2:
                print("\nНевірні числа")
                continue
            
            print("\nКількість щасливих квитків:", func.luc_tickets(num_1, num_2))
            
        elif choise == 3:
            print("До побачення!")
            break
        
        else:
            print("\nНе вірний номер функції виберіть від 1 до 4")
            continue
        
if __name__ == "__main__":
    main()
    