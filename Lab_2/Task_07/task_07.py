from func_modul import ask_month # Імпорт функції з іншого файлу

def main():
    """Основна функція яка передає номер місяця в функцію\n
    ask_month та виводить його назву"""
    
    nam_month = int(input("Введіть номер місяця: ")) # введення номера місяця
    ask_month(nam_month) # виклик функції
    
if __name__ == "__main__": # Перевірка чи файл був запущений напряму
    main() # Виклик основної функції
    
