from class_Vehicle import Vehicle

# Приклад роботи з класом Vehicle
class Airplane(Vehicle): # Клас Літак, що наслідує клас Транспортний засіб
    def __init__ (self, price, speed, year_release, height, passengers): 
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        :param height: Висота
        """
        super().__init__(price, speed, year_release, passengers=passengers, height=height) # Ініціалізація атрибутів класу
        
    def __str__(self): # Метод для виводу інформації про літак
        """
        Виводить інформацію про літак
        :return: Інформація про літак
        """
        return f"Літак:\n {super().__str__()}"
    
class Car(Vehicle):
    def __init__ (self, price, speed, year_release, passengers): # Клас Автомобіль, що наслідує клас Транспортний засіб
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        :param passengers: Кількість пасажирів
        """
        super().__init__(price, speed, year_release, passengers=passengers)
    
    def __str__(self): # Метод для виводу інформації про автомобіль
        """
        Виводить інформацію про автомобіль
        :return: Інформація про автомобіль
        """
        return f"Автомобіль:\n {super().__str__()}"
    
class Ship(Vehicle):
    def __init__ (self, price, speed, year_release, passengers, port): # Клас Корабель, що наслідує клас Транспортний засіб
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        :param passengers: Кількість пасажирів
        :param port: Порт приписки
        """
        super().__init__(price, speed, year_release, passengers=passengers, port=port)
    
    def __str__(self): # Метод для виводу інформації про корабель
        """
        Виводить інформацію про корабель
        :return: Інформація про корабель
        """
        return f"Корабель:\n {super().__str__()}"

def main():
    menu = {
        1: "Літак",
        2: "Автомобіль",
        3: "Корабель",
        0: "Вихід"
    }
    
    while True:
        print("\nВиберіть тип транспортного засобу:")
        for key in menu:
            print(f"{key}: {menu[key]}")
        
        choice = int(input("Ваш вибір: "))
        
        if choice == 0:
            print("Вихід з програми")
            break
        
        elif choice == 1:
            price = float(input("Введіть вартість: "))
            speed = float(input("Введіть швидкість: "))
            year_release = int(input("Введіть рік випуску: "))
            height = float(input("Введіть висоту літака: "))
            passengers = int(input("Введіть кількість пасажирів: "))
            airplane = Airplane(price, speed, year_release, height, passengers)
            x = float(input("Введіть координату X: "))
            y = float(input("Введіть координату Y: "))
            airplane.set_coordinates(x, y)
            print("\nДанні про літак: ", airplane)
            
        elif choice == 2:
            price = float(input("Введіть вартість: "))
            speed = float(input("Введіть швидкість: "))
            year_release = int(input("Введіть рік випуску: "))
            passengers = int(input("Введіть кількість пасажирів: "))
            car = Car(price, speed, year_release, passengers)
            x = float(input("Введіть координату X: "))
            y = float(input("Введіть координату Y: "))
            car.set_coordinates(x, y)
            print("\nДанні про автомобіль: ", car)
            
        elif choice == 3:
            price = float(input("Введіть вартість: "))
            speed = float(input("Введіть швидкість: "))
            year_release = int(input("Введіть рік випуску: "))
            passengers = int(input("Введіть кількість пасажирів: "))
            port = input("Введіть порт приписки: ")
            ship = Ship(price, speed, year_release, passengers, port)
            x = float(input("Введіть координату X: "))
            y = float(input("Введіть координату Y: "))
            ship.set_coordinates(x, y)
            print("\nДанні про корабель: ", ship)
        else:
            print("Неправильний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()
            
    
    
    
    
    
