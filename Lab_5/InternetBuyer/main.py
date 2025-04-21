from class_InternetBuyer import InternetBuyer

def main():
    print("Вітаємо в інтернет-магазині!")
    print("Будь ласка, введіть свої дані для реєстрації\n")
    name = input("Введіть Ім'я: ")
    phone = input("Введіть номер телефону: ")
    birth_date = input("Введіть дату народження (ДД.ММ.РРРР): ")
    sex = input("Введіть стать (чоловіча/жіноча): ")
    email = input("Введіть електронну пошту: ")

    buer = InternetBuyer(name, phone, birth_date, sex, email)

    # Додамо товар до кошика
    while True:    
        item = input("\nВведіть товар, який хочете додати до кошика: ")
        print("Для завершення введіть залиште поле порожнім")
        if item == "":
            break
            
        buer.add_to_shop_cart(item) # Додамо товар до кошика
        buer.add_to_bay_history(item)  # Додамо товар до історії покупок

    # Вибір способу доставки
    print("Доступні способи доставки:")
    for metod in buer.delivery_methods:
        print(metod)
    delivery = input("Оберіть спосіб доставки: ")
    buer.set_delivery_methods(delivery)

    # Введення адреси доставки
    address = input("Введіть адресу доставки: ")
    buer.set_delivery_address(address)

    print("\nДанні про покупця:")
    print(buer)
    print("Дякуємо за покупку!")

if __name__ == "__main__":
    main()

