# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
from random import randint

# Первое решение

N = int(input("Enter the length of your array: "))
x = int(input("Enter the num, which you want to find: "))
my_list = [i + 1 for i in range(N)]
print(my_list)

for i in my_list:
    if i == x:
        print(i)
    else:
        if x > my_list[-1]:
            print(my_list[-1])
            break
        elif x < my_list[0]:
            print(my_list[0])
            break

# Второе решение

# N = int(input("Enter the length of your array: "))
# if N < 0:
#     N = abs(N)
# max_num = int(input("Enter max positive num in your list: "))
# if max_num < 0:
#     max_num = abs(max_num)
# x = int(input("Enter the positive num, which you want to find: "))
# if x < 0:
#     x = abs(max_num)
#
# if max_num < 0 or x < 0:
#     print("Error! Enter the positive num")
# my_list = [randint(1, max_num) for i in range(N)]
# print(my_list)
#
# my_dict = {}
# new_list = []
# new_list_2 = []
#
# for i in my_list:
#     my_dict[i] = x - i
# n = sorted(my_dict.values())
# # print(my_dict)
# # print(n)
#
# for k in n:
#     if k < 0:
#         new_list.append(k)
#     else:
#         new_list_2.append(k)
# # print(new_list)
# # print(new_list_2)
#
# for i in new_list:
#     i = abs(i)
#     new_list_2.append(i)
# # print(new_list_2)
#
# for i in new_list_2:
#     i = i * -1
#     new_list.append(i)
# # print(new_list)
#
# a = new_list[-1]
# b = new_list_2[0]
# if a == 0:
#     result = a
#     # print(a)
# elif b == 0:
#     result = b
#     # print(b)
# elif abs(a) < b:
#     result = a
#     # print(a)
# else:
#     result = b
#     # print(b)
#
# for k, v in my_dict.items():
#     if v == result:
#         print(k)
