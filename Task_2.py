### Task 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#### Вариант решения 1 (список изначально  задан) ###########

# numbers = [2, 3, 4, 5, 6]
# list = []
# for i in range(len(numbers)):
#     if i < len(numbers) / 2:
#         list.append(numbers[i] * numbers[-i-1])
# print(list)

#### Вариант решения 2 (список вводит пользователь) ###########

numbers = input("Введите список чисел, разделенных пробелом: ").split()
numbers_int = list(map(int, numbers))

list = []
for i in range(len(numbers_int)):
    if i < len(numbers_int) / 2:
        list.append(numbers_int[i] * numbers_int[-i-1])
print(list)

