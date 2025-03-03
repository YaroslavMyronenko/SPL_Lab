import random
while True:
    n = int(input("Введіть кількість елементів масиву: "))

    array = [round(random.uniform(-10, 10),2)for _ in range(n)]
    negative_num = [num for num in array if num < 0]

    print(f"Початковий масив\n{array}")
    print(f"\nМаксимальний елемент: {max(array)}\n")
    print("Середнє арефметичне відємних елементів масиву:", sum(negative_num) / len(negative_num) if negative_num else "0\n")
    print(f"\nМасив у зворотньому порядку: \n{array[::-1]}\n")

    choice = input("Хочете продовжити? (Введіть так): ")
    if choice not in ("так", "yes", "y", "т"):
        print("Програма завершена.")
        break