#!/usr/bin/env python3
#coding: utf-8
#
#author:SwordsDevil
#date:2019/08/05
#usage:some for statement

#死循环
# while True:
#     hen = input("please input name:")
#     if hen == "SwordsDevil":
#         break

list = [1, 3.14, True, False, "String Type"]

for i in range(len(list)):
    print(list[i])

for i in list:
    print(i)

