# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def raiseToThePower (a, b):
    if b == 0:
        return 1
    return a * raiseToThePower(a, b-1)

a = int(input("Введите число А"))
b = int(input("Введите число B"))
print (raiseToThePower(a, b))