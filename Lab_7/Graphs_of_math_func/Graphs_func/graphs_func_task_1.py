import matplotlib.pyplot as plt # імпортуємо бібліотеку для побудови графіків
import numpy as np # імпортуємо бібліотеки для матиматичних обчислень та створення масиву

# фукнкція для обчислення функції 
def graph_func():
    """Функція для обчислення значень функції Y(x)=5*sin(10*x)*sin(3*x)"""
    
    x = np.linspace(0, 4, 200) # створюємо масив x від 0 до 4 з 100 точками
    y = 5 * np.sin(10 * x) * np.sin(3 * x) # обчислюємо y за формулою
    return x, y # повертаємо масиви x та y

def main():
    # створюємо графік
    x, y = graph_func() # отримуємо масиви x та y

    plt.plot(x, y, label='Y(x)=5*sin(10*x)*sin(3*x)', 
            linestyle='--', color='red', marker='.', 
            markerfacecolor='pink', markeredgecolor='black', 
            ms=8, lw=2) # будуємо графік

    plt.title("Графік функції: Y(x)=5*sin(10*x)*sin(3*x)") # додаємо заголовок
    plt.xlabel("X") # додаємо підпис до осі x
    plt.ylabel("Y") # додаємо підпис до осі y
    plt.legend() # додаємо легенду
    plt.axhline(0, color='blue', linestyle='--', lw=2) # додаємо горизонтальну лінію y=0
    plt.axvline(0, color='green', linestyle='--', lw=2) # додаємо вертикальну лінію x=0
    plt.savefig("Graphs_of_math_func/Graphs_png/graph_func_task_1.png") # зберігаємо графік у файл 
    plt.show() # показуємо графік

if __name__ == "__main__":
    main() # викликаємо основну функцію

