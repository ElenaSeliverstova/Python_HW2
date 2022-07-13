# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number_N = int(input("Введите вещественное число: "))
list_of_numbers = [1]
for i in range(1, number_N):
    list_of_numbers.append(list_of_numbers[i-1]*(i+1))
print(list_of_numbers)