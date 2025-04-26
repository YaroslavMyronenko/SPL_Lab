class Vehicle: # Абстрактний клас Транспортний засіб
    def __init__(self, name, price, speed, year_release, passengers=0, height=0, port=None):
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        """
        self.name = name # Назва
        self.price = price # Вартість
        self.speed = speed # Швидкість
        self.year_release = year_release # Рік випуску
        self.coordinates = (0, 0) # Координати
        self.passengers = passengers # Кількість пасажирів
        self.height = height # Висота
        self.port = port # Порт приписки
        
    
    def set_coordinates(self, x, y): # Метод для встановлення координат
        """
        Встановлює координати
        :param x: Координата X
        :param y: Координата Y
        """
        self.coordinates = (x, y)
    
    def __str__(self):
        return (f"Вартість: {self.price}$ \nШвидкість: {self.speed}km/h \nРік випуску: {self.year_release} "
                f"\nКоординати: {self.coordinates} \nКількість пасажирів: {self.passengers} чоловік "
                f"\nВисота: {self.height}м \nПорт приписки: {self.port}")