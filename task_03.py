# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

number_n = int(input("Enter n: "))
dictionaty_of_function = {}
for i in range(1, number_n+1):
    dictionaty_of_function[i] = (1+1/i)**i
print(dictionaty_of_function)