from class_Vehicle import Vehicle

# Приклад роботи з класом Vehicle
class Airplane(Vehicle): # Клас Літак, що наслідує клас Транспортний засіб
    def __init__ (self, name, price, speed, year_release, height, passengers): 
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        :param height: Висота
        """
        super().__init__(name, price, speed, year_release, passengers=passengers, height=height) # Ініціалізація атрибутів класу
        
    def __str__(self): # Метод для виводу інформації про літак
        """
        Виводить інформацію про літак
        :return: Інформація про літак
        """
        return (f"\n{self.name}:\n"
                f"Вартість: {self.price} $\n"
                f"Швидкість: {self.speed} km/h\n"
                f"Рік випуску: {self.year_release} р.\n"
                f"Координати: {self.coordinates}\n"
                f"Кількість пасажирів: {self.passengers} чоловік\n"
                f"Висота: {self.height}м")
    
class Car(Vehicle):
    def __init__ (self, name, price, speed, year_release): # Клас Автомобіль, що наслідує клас Транспортний засіб
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        :param passengers: Кількість пасажирів
        """
        super().__init__(name, price, speed, year_release)
    
    def __str__(self): # Метод для виводу інформації про автомобіль
        """
        Виводить інформацію про автомобіль
        :return: Інформація про автомобіль
        """
        return (f"\n{self.name}:\n"
                f"Вартість: {self.price} $\n"
                f"Швидкість: {self.speed} km/h\n"
                f"Рік випуску: {self.year_release} р.\n"
                f"Координати: {self.coordinates}\n")
    
class Ship(Vehicle):
    def __init__ (self, name, price, speed, year_release, passengers, port): # Клас Корабель, що наслідує клас Транспортний засіб
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        :param passengers: Кількість пасажирів
        :param port: Порт приписки
        """
        super().__init__(name, price, speed, year_release, passengers=passengers, port=port)
    
    def __str__(self): # Метод для виводу інформації про корабель
        """
        Виводить інформацію про корабель
        :return: Інформація про корабель
        """
        return (f"\n{self.name}:\n"
                f"Вартість: {self.price} $\n"
                f"Швидкість: {self.speed} km/h\n"
                f"Рік випуску: {self.year_release} р.\n"
                f"Координати: {self.coordinates}\n"
                f"Кількість пасажирів: {self.passengers} чоловік\n"
                f"Порт приписки: {self.port}")

def input_positive_int(number):
    while True:
        value = input(number)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Введіть додатнє число!")

def input_positive_float(number):
    while True:
        try:
            value = float(input(number))
            if value > 0:
                return value
            print("Введіть додатнє число!")
        except ValueError:
            print("Введіть коректне число!")
            
def input_year(date):
    while True:
        value = input(date)
        if value.isdigit() and 1900 <= int(value) <= 2025:
            return int(value)
        print("Введіть коректний рік!") 

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
            name = input("Введіть модель транспортного засобу: ")
            price = input_positive_float("Введіть вартість: ")
            speed = input_positive_float("Введіть швидкість: ")
            year_release = input_year("Введіть рік випуску: ")
            height = input_positive_float("Введіть висоту літака: ")
            passengers = input_positive_int("Введіть кількість пасажирів: ")
            airplane = Airplane(name, price, speed, year_release, height, passengers)
            x = input_positive_float("Введіть координату X: ")
            y = input_positive_float("Введіть координату Y: ")
            airplane.set_coordinates(x, y)
            print("\nДанні про літак: ", airplane)
            
        elif choice == 2:
            name = input("Введіть модель транспортного засобу: ")
            price = input_positive_float("Введіть вартість: ")
            speed = input_positive_float("Введіть швидкість: ")
            year_release = input_year("Введіть рік випуску: ")
            car = Car(name, price, speed, year_release)
            x = input_positive_float("Введіть координату X: ")
            y = input_positive_float("Введіть координату Y: ")
            car.set_coordinates(x, y)
            print("\nДанні про автомобіль: ", car)
            
        elif choice == 3:
            name = input("Введіть модель транспортного засобу: ")
            price = input_positive_float("Введіть вартість: ")
            speed = input_positive_float("Введіть швидкість: ")
            year_release = input_year("Введіть рік випуску: ")
            passengers = input_positive_int("Введіть кількість пасажирів: ")
            port = input("Введіть порт приписки: ")
            ship = Ship(name, price, speed, year_release, passengers, port)
            x = input_positive_float("Введіть координату X: ")
            y = input_positive_float("Введіть координату Y: ")
            ship.set_coordinates(x, y)
            print("\nДанні про корабель: ", ship)
        else:
            print("Неправильний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()