import math

x = int(input("Введіть ціле число: "))
if x > 45: 
    z = -math.sqrt(x)
elif x <= 45:
    z = math.sin(2*x)
print(z)          
print("Натисніть Enter для виходу...")
input()
print("Программа завершена.")