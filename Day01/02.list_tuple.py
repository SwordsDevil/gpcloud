#/usr/bin/env python3
#coding = utf-8
#
#author:SwordsDevil
#date:2019/08/05
#usage: study list and tuple

list01 = [123, 23.31, "chen", True]
tuple01 = (123, 23.321, "wen", False)

list01_size = list01.__sizeof__()
tuple01_size = tuple01.__sizeof__()

print("list's size:{}".format(list01_size))
print("tuple's size:{}".format(tuple01_size))

list01.append("world")
print("list's len:{}".format(len(list01)))
print("tuple's len:{}".format(len(tuple01)))

print(type(list01[3]))
print(list01[2:3])
print(list01[0:])
print(list01[:3])
print(list01[0:4:2])




