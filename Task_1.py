# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#### Вариант решения 1 (список изначально  задан) ###########

# numbers = [2, 3, 5, 9, 3]
# sum_digits = 0
# # print(len(numbers))
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         sum_digits += numbers[i]
# print(sum_digits)

#### Вариант решения 2 (список вводит пользователь) ###########
numbers = input("Введите список чисел, разделенных пробелом: ").split()
numbers_int = list(map(int, numbers)) # функция map работает как цикл for перебирая элементы и преобразует их в нужный тип данных
sum_digits = 0
for i in range(len(numbers_int)):
    if i % 2 != 0:
        sum_digits += numbers_int[i]
print(sum_digits)


