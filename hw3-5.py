# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



def fib(n):
    if n in [1, 2]:                       
        return 1
    else:
        return fib(n-1) + fib(n-2)

def nfib(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        n1, n2 = 1, -1
        for i in range(2, n):
            n1, n2 = n2, n1 - n2
        return n2

list = [0]
n = int(input('введите число: '))
for i in range(1, n + 1):
    list.append(fib(i))
    list.insert(0, nfib(i))
print(list)