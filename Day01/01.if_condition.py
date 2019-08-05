#/usr/bin/env python3
#coding:utf-8
#
#author:SwordsDevil
#date:2019/08/05
#usage:study


# var01 = 1
# var01 = str(var01)
# print(var01,type(var01))

# for i in range(1,201):
#     if i % 7 == 0 and i % 6 == 5 and i % 5 == 4 and i % 3 == 2 and i % 2 == 1:
#         print(i)

# readline = input('please input number:')
# line = int(float(readline))
# print(type(line),line)
# -- 找出素数
# for i in range(2,101):
#     for j in range(2,i):
#        if  i % j == 0:
#            break
#     else:
#         print(i)

# -- 输入两个值并相加
# a = int(input('input a:'))
# b = int(input('input b:'))
# print(a+b)

# -- 输入两个数并比较大小
# a = int(input('input a:'))
# b = int(input('input b:'))
#
# if a > b :
#     print(a)
# else:
#     print(b)

# -- 列出公约数
# if a>b :
#     for i in range(1,b + 1):
#         if a % i == 0 and b % i == 0:
#             print(i)
# else:
#     for i in range(1,a + 1):
#         if a % i == 0 and b % i == 0:
#             print(i)


# if a > b :
#     x = a % b
#     while x != 0:
#         a = b
#         b = x
#         x = a % b
#     print(b)

list01 = [ 12, 213.3, "str", True]
list01_size = list01.__sizeof__()
print(len(list01))
print(list01_size)


