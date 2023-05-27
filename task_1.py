# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

# Первое решение

N = int(input("Enter the length of your array: "))
x = int(input("Enter the num, which you want to find: "))
my_list = [i + 1 for i in range(N)]
print(my_list)

count = 0
for i in my_list:
    if i == x:
        count += 1
print(count)

# Второе решение

# N = int(input("Enter the length of your array: "))
# max_num = int(input("Enter max num in your list: "))
# x = int(input("Enter the num, which you want to find: "))
# my_list = [randint(1, max_num) for i in range(N)]
# print(my_list)
#
# count = 0
# for i in my_list:
#     if i == x:
#         count += 1
# print(count)
