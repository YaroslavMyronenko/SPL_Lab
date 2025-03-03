while True:
    p = int(input("\nВведіть число р: "))
    F0, F1 = 1, 1 

    while F1 <= p:
        F0, F1 = F1, F0 + F1
    print(f"Перше число Фібоначі, більше за р({p}): {F1}")

    choice = input("Хочете продовжити? (Введіть так): ")
    if choice not in ("так", "yes", "y", "т"):
        print("Програма завершена.")
        break
