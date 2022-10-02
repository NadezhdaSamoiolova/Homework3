# Task 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]
list = []
for i in range(len(numbers)):
    list.append(round(numbers[i] % 1, 2))
print('Your list is :', list)
list.remove(0)
print('Your list without 0-digits is :', list)
max_element = max(list)
print('Your max element is: ', max_element)
min_element = min(list)
print('Your min element is: ', min_element)
print('Your result is: ', max_element-min_element)


