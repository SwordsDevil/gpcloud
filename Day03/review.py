#!/usr/bin/env python3
#coding:utf8
#usage: review dict and set

#dict define
dict01 = {'name':'chenwenbin','age':18,'sex':'male'}
dict02 = dict({'name': 'SwordsDevil', 'age': 18,'sex': 'male'})
dict03 = dict([('name','SwordsDevil'),('age',18),('sex','male')])
dict04 = dict(name='SwordsDevil',age=18,sex = 'male')
print(dict01)
print(dict02)
print(dict03)
print(dict04)

#dict method
keys = dict01.keys()
print(keys)
values = dict02.values()
print(values,type(values))
items = dict03.items()
print(items)
dict04.pop('age')
print(dict04)
print(dict04['name'])
dict04.setdefault('age',20)
print(dict04)
dict04.update([('age',30)])
print(dict04)

#set define and method
set = {'name','some','go',15}
print(set)
set.update(['chen'])
print(set)
set.remove(15)
print(set)
set.add('wen')
print(set)