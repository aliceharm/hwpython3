#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [56, 2, 1, -5, -3, 8, -1]


import math 
par = math.ceil(len(list)/2)

list2 = []
for i in range(par):
    list2.append(list[i]*list[-i - 1])
print(list2)