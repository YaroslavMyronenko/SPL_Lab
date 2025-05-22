def clean_list(list_to_clean):
    """
    Функція яка приймає список будь яких значень і 
    повертає список без дублікатів
    """
    
    # Перевіряємо чи список не пустий
    if not list_to_clean:
        print ("Список пустий")
        return []
    
    # Створюємо новий список без дублікатів
    new_clean_list = []
    for item in list_to_clean:
        if item not in new_clean_list:
            new_clean_list.append(item)
            
    return new_clean_list

def counter(a, b):
    """
    Функція приймає два цілі невідємні аргументи та 
    повертає кількість різних цифр числа b які містяться в числі a
    """
    
    # Перевіряємо чи числа не від'ємні і не нулеві
    if a < 0 or b < 0 and a != 0 and b != 0:
        print ("Числа повинні бути невід'ємними і не нульовими")
        return 0

    # Перевіряємо чи числа не пусті
    if not a or not b:
        print ("Числа пусті")
        return 0
    
    # Знаходимо різні цифри числа b які містяться в числі a
    a_digits = set(str(a)) # Перетворюємо число a в строку
    b_digits = set(str(b)) # Перетворюємо число b в строку

    digits = a_digits & b_digits # Знаходимо спільні цифри
    return len(digits) # Повертаємо кількість спільних цифр

def find_most_frequent(text):
    """
    Функція якаа приймає будь який текст і повертає
    слова у нижньому регістрі яке зустрічається найчастіше"""
    
    # Перевіряємо чи текст не пустий
    if not text: 
        print ("Текст пустий")
        return []
    
    # Прибираємо всі непотрібні пробіли та знаки пунктуації
    symvols = "!@#$%^&*()_+-=~`<>? ,./:;{}[]|\\\"'"
    
    for s in symvols: # Очищення тексту від непотрібних символів та знаків пунктуації
        text = text.replace(s, ' ')
    
    # Розбиваємо текст на слова та приводимо до нижнього регістру
    words = text.split() # Розділення тексту на слова
    
    # Знаходимо слово яке зустрічається найчастіше
    most_frequent_word = None
    max_count = 0
    for word in words: 
        word = word.lower()
        count = words.count(word) 
        if count > max_count: 
            max_count = count 
            most_frequent_word = word
            
    return most_frequent_word


