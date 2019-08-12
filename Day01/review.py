#!/usr/bin/env python3
#coding:utf8

tuple01 = (1,2,4,'chen','wen',True,[1,2,3],1)
print(tuple01)
list01 = tuple01[6]
list01.append(4)
print(tuple01)
print(list01)


tuple_size = tuple01.__sizeof__()
print(tuple01.__sizeof__())
print(len(tuple01))
print(tuple01.count(1))
print(tuple01.index(1))

#遍历出相同元素的所有索引
indexs =[i for i,tuple01 in enumerate(tuple01) if tuple01 == 1]
print(indexs)

x = enumerate(tuple01)
print(list(x))

# for i in range(len(tuple01)):
#     print(tuple01[i])

# for element in tuple01:
#     print(element)

list02 = [1,2,5,'hello','chen',3,True,0,'wen']
print(list02)

list02.append('bin')
print(list02)
list02.insert(4,'world')
print(list02)
list02.remove(1)
print(list02)
list02.insert(0,1)
list02.pop(0)
print(list02)
list02.extend(list01)
print(list02)
list01.reverse()
print(list01)
list01.sort()
print(list01)
list01.clear()
print(list01)
del list01


str01 = 'chen wen bin'
str02 = 'www.baidu.com'
name = str01.split()
domain = str02.split('.')
print(name,domain)
name01 = str01.replace(' ','')
print(name01)
str01 = ' chen wen bin '
print(str01)
space = str01.strip()
print(space)
