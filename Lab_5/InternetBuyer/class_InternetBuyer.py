class InternetBuyer: 
    """
    Клас «Інтернет-покупець»
    Клас, в якому зберігатиметься інформація про інтернет-покупця така як ім’я,
    номер телефону, день народження, стать, електронна пошта, метод для збереження історії
    покупок, метод для кошику покупців, та метод для можливості вказання способу та адреси доставки
    """
    def __init__(self, name, phone, birth_date, sex, email): # Ініціалізація атрибутів класу
        self.name = name # Ім'я покупця
        self.phone = phone # Номер телефону
        self.birth_date = birth_date # Дата народження
        self.sex = sex # Стать
        self.email = email # Електронна пошта
        self.bay_history = [] # Історія покупок
        self.shop_cart = [] # Кошик покупця
        self.delivery = None # Спосіб доставки
        self.delivery_methods = ['Нова Пошта', 'УкрПошта', 'Justin'] # Доступні способи доставки
        self.delivery_address = {}
        
    def add_to_bay_history(self, item): # Метод для збереження історії покупок
        """
        Додає товар до історії покупок
        :param item: Товар, який потрібно додати до історії покупок
        """
        self.bay_history.append(item) # Історія покупок
    
    def add_to_shop_cart(self, item): # Метод для кошику покупців
        """
        Додає товар до кошика покупця
        :param item: Товар, який потрібно додати до кошика
        """
        self.shop_cart.append(item) # Кошик покупця
        print(f"Товар {item} додано до кошика") 
        
    def set_delivery_methods(self, delivery):
        """
        Встановлює спосіб доставки
        :param delivery: Спосіб доставки
        """
        if delivery in self.delivery_methods: # Якщо спосіб доставки є в списку доступних способів доставки
            self.delivery = delivery
        else:
            print("Неправильний спосіб доставки!")
        
    def set_delivery_address(self, address):
        """
        Встановлює адресу доставки
        :param address: Адреса доставки
        """
        self.delivery_address = address
        print(f"Адреса доставки {self.delivery_address} обрана")
        
    def __str__(self): # Метод для виводу інформації про покупця
        """
        Виводить інформацію про покупця
        :return: Інформація про покупця
        """
        return f"\nІм'я: {self.name} \nНомер телефону: {self.phone} \nДата народження: {self.birth_date}  \nСтать: {self.sex} \nЕлектронна пошта: {self.email} \nІсторія покупок: {self.bay_history} \nКошик покупця: {self.shop_cart} \nСпосіб доставки: {self.delivery} \nАдреса доставки: {self.delivery_address}"
        
    
    
       
        

        
    
        
        
        
        
        
