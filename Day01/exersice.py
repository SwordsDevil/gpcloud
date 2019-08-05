#/usr/bin/env python3
#coding= utf-8
#
#author:SwordsDevil
#date:2019/08/05
#usage:exercise about some statement



#找出1到100的所有素数
# for i in range(2,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# --求出两个数的最大公约数
# a = int(input("please input a:"))
# b = int(input("please input b:"))
#
# if a>b :
#     x = a % b
#     while x != 0:
#         a = b
#         b = x
#         x = a % b
#     print(b)
# else:
#     x = b % a
#     while x != 0:
#         b = a
#         a = x
#         x = b % a
#     print(a)

# --求两个数的最小公倍数
# a = int(input("input a:"))
# b = int(input("input b:"))
#
# if a > b :
#     c = a
# else:
#     c = b
#
# while True:
#     if c % a == 0 and c % b == 0:
#         print(c)
#         break
#     c +=1

# --求1~100的和
# s = 0
# for x in range(1,101):
#     s = s + x
# print(s)

# -- 1~10的乘积
s = 1
for x in range(1,11):
    s *= x
print(s)