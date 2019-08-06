#!/usr/bin/env python3
# coding = utf-8
#
#author:SwordsDevil
#date:2019/08/06
#usage: list function


list01 = [1, 3.14, 1, False, True, "devil"]

#打印某元素的数量
number = list01.count(1)
print(number)

#查找某一元素的索引
index = list01.index(1,1,4)
print(index)

#在列表最后面追加元素
list01.append("Swords")
print(list01)

#插入元素
list01.insert(1,"hello")
print(list01)

#将一个列表拓展到另一个列表
list02 = [2, 4, 7]
list01.extend(list02)
print(list01)

#删除根据索引号
list01.pop(3)
print(list01)

#根据元素删除
list01.remove(False)
print(list01)

#对列表进行排序
list03 = [23,53,13, 43,25,11,32,8]
list03.sort()
print(list03)


#对列表进行反转
list03.reverse()
print(list03)

