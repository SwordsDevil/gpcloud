#!/usr/bin/env python3
#coding = utf-8
#

tuple01 = (1,2.23,2,6,"hello",True)

print("tuple01.size:{}".format(tuple01.__sizeof__()))
number = tuple01.count(1)
print(number)
index = tuple01.index(6)
print(index)

# for i in range(len(tuple01)):
#     print(tuple01[i])

for element in tuple01:
    print(element)


list01 = [1,3.32,4,2,"hello",True,False]

list01.append("chen")
print(list01)
list01.insert(2,"wen")
print(list01)
list02 = [2,4,"world"]
list01.extend(list02)
print(list01)

list01.remove(2)
print(list01)

list01.pop(2)
print(list01)

list03 = [12,52,3,23,45,76,21]
list03.sort()
print(list03)

list03.reverse()
print(list03)
list02.clear()
print(list02)


