# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list = [1, 4, 15, 3, 6, 12, 19]
min = int(input("Введите минимальное число диапазона "))
max = int(input("Введите максимальное число диапазона 3"))
list_index = []
for i in range(len(list)):
    if list[i] >= min and list[i] <= max:
        list_index.append(i)
    i += 1
print(list_index)