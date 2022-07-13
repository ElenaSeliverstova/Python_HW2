# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number_N = int(input("Введите вещественное число: "))
result = 0
while number_N > 0:
    digit = number_N % 10
    result += digit
    number_N = number_N // 10
print(result)