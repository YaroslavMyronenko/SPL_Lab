class Vehicle: # Абстрактний клас Транспортний засіб
    def __init__(self, price, speed, year_release, passengers=0, height=0, port=None):
        """
        Ініціалізація атрибутів класу
        :param price: Вартість
        :param speed: Швидкість
        :param year_release: Рік випуску
        """
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
        print(f"Координати встановлено: {self.coordinates}")
        
    def get_coordinates(self): # Метод для отримання координат
        """
        Отримує координати
        :return: Координати
        """
        return self.coordinates
    
    def set_price(self, price): # Метод для встановлення вартості
        """
        Встановлює вартість
        :param price: Вартість
        """
        self.price = price
        print(f"Вартість встановлено: {self.price}")   
        
    def get_price(self): # Метод для отримання вартості
        """
        Отримує вартість
        :return: Вартість
        """
        return self.price
    
    def set_speed(self, speed): # Метод для встановлення швидкості
        """
        Встановлює швидкість
        :param speed: Швидкість
        """
        self.speed = speed
        print(f"Швидкість встановлено: {self.speed}")
        
    def get_speed(self): # Метод для отримання швидкості
        """
        Отримує швидкість
        :return: Швидкість
        """
        return self.speed
    
    def set_year_release(self, year_release): # Метод для встановлення року випуску
        """
        Встановлює рік випуску
        :param year_release: Рік випуску
        """
        self.year_release = year_release
        print(f"Рік випуску встановлено: {self.year_release}")
    
    def get_year_release(self): # Метод для отримання року випуску
        """
        Отримує рік випуску
        :return: Рік випуску
        """
        return self.year_release
    
    def set_passengers(self, passengers): # Метод для встановлення кількості пасажирів
        """
        Встановлює кількість пасажирів
        :param passengers: Кількість пасажирів
        """
        self.passengers = passengers
        print(f"Кількість пасажирів встановлено: {self.passengers}") 
        
    def get_passengers(self): # Метод для отримання кількості пасажирів
        """
        Отримує кількість пасажирів
        :return: Кількість пасажирів
        """
        return self.passengers
    
    def set_height(self, height): # Метод для встановлення висоти
        """
        Встановлює висоту
        :param height: Висота
        """
        self.height = height
        print(f"Висота встановлено: {self.height}")
           
    def get_height(self): # Метод для отримання висоти
        """
        Отримує висоту
        :return: Висота
        """
        return self.height
    
    def set_port(self, port): # Метод для встановлення порту приписки
        """
        Встановлює порт приписки
        :param port: Порт приписки
        """
        self.port = port
        print(f"Порт приписки встановлено: {self.port}")
        
    def get_port(self): # Метод для отримання порту приписки
        """
        Отримує порт приписки
        :return: Порт приписки
        """
        return self.port
    
    def __str__(self): # Метод для виводу інформації про транспортний засіб
        """
        Виводить інформацію про транспортний засіб
        :return: Інформація про транспортний засіб
        """
        return f"Вартість: {self.price} \nШвидкість: {self.speed} \nРік випуску: {self.year_release} \nКоординати: {self.coordinates} \nКількість пасажирів: {self.passengers} \nВисота: {self.height} \nПорт приписки: {self.port}"
    

            
    