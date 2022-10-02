# Task 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


n = int(input('Input a number: '))  
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
list = []

for i in range(1, n + 1):
    list.append(fibonacci(i))

n = n* -1
def negaFibonacci(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return negaFibonacci(n+2) - negaFibonacci(n+1)

for i in range(n , 0):
    list.insert(n, negaFibonacci(i))
list.insert(n, 0)

print(list)

