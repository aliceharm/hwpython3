# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

list = [5.2, 5.4, 0.15, 1, 0.01]
list1 = []
for i in range(len(list)):
    if list[i]%1 != 0:
        list1.append(round(list[i]%1,2))

print(round(max(list1) - min(list1),2))