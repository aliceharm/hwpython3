#Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной идексах.


list = [34, -56, 12, 23, -2, 16, 56, -9]

s = 0
for i in range(1, len(list), 2):
            s += list[i]       
print(s)