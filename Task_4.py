# Task 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Input a number: '))
# print(bin(n))
a = str(bin(n))
result_a = "" 
for i in range(0, len(a)): 
    if i > 1 : 
        result_a = result_a + a[i] 
print ('Your result is: ' + result_a)

