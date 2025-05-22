from Function_lib import clean_list, counter, find_most_frequent

def main():
    
    menu = {
        1: "Очистити список від дублікатів",
        2: "Порахувати кількість різних цифр числа b які містяться в числі a",
        3: "Знайти слово яке зустрічається найчастіше",
        4: "Вийти з програми"
    }
    
    while True:
        for key, value in menu.items():
            print(f"{key}: {value}")
            
        choise = input("\nОберіть функцію: ")
        if not choise.isdigit():
            print("\nНомер повинен бути числом від 1 до 4")
            continue
        
        choise = int(choise)
        if choise not in menu:
            print("\nНе вірний номер функції виберіть від 1 до 4")
            continue
        
        if choise == 1:
            list_to_clean = input("Введіть список через пробіл: ").split()
            print("\nСписок без дублікатів:", clean_list(list_to_clean))
            
        elif choise == 2:
            a = int(input("Введіть число a: "))
            b = int(input("Введіть число b: "))
            print("\nКількість різних цифр числа b які містяться в числі a:", counter(a, b))
            
        elif choise == 3:
            text = input("Введіть текст: ")
            print("\nСлово яке зустрічається найчастіше:", find_most_frequent(text))
            
        elif choise == 4:
            print("До побачення!")
            break
        
        else:
            print("\nНе вірний номер функції виберіть від 1 до 4")
            continue
        
if __name__ == "__main__":
    main()
    
    
    
        