"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    return x ** y


a, b = int(input("Введите положительное число: ")), int(input("Введите отрицательное число: "))

print(my_func(a, b))