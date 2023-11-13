import numpy as np

number = int(input("Введите число слов  "))
language = input("Выберите язык ввода [RU/EN]  ")

words = {}
with open('word.txt', encoding = 'utf-8') as f:
    for line in f.readlines():
        words[line.split(':')[0].strip().lower()] = line.split(':')[1].strip().lower()

print('\n' * 5)
for word in range(number):
    eng = np.random.choice(list(words.keys()))
    rus = words[eng]

    if language.upper() == 'RU':
        if input(f"{eng.capitalize()}:  ").strip().lower() != rus:
            print(f"ЛАЖА. {rus}")

    elif language.upper() == 'EN':
        if input(f"{rus.capitalize()}:  ").strip().lower() != eng:
            print(f"ЛАЖА. {eng}")

