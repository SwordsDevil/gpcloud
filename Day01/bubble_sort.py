#!/usr/bin/env python3
# coding=utf-8
#
#author:SwordsDevil
#date:2019/08/05
#usage: bubble sort


list01 = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]

for i in range(len(list01)):
    j = 0
    while j < len(list01)-1:
        if list01[j] > list01 [j+1]:
            list01[j],list01[j+1] = list01[j+1],list01[j]
        j +=1
print(list01)


for i in range(len(list01)):
    for j in range(len(list01) -i -1):
        if list01[j] > list01[j+1]:
            list01[j],list01[j+1] = list01[j+1], list01[j]