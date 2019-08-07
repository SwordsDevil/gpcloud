#!/usr/bin/env python3
#coding = utf-8

#对字符串进行反转
string01 = "this is my house"
list01 = string01.split()
list01.reverse()
#string02 = list01[0]+" "+list01[1]+" "+list01[2]+" "+list01[3]
#print(string02)
string02 = ""
# for element in list01:
#     string02 +=(element +" ")
# print(string02.rstrip())
i = 0
while i< len(list01):
    string02 += list01[i] + " "
    i += 1
print(string02.rstrip())


#敏感词替换
# search = input("please input your search：")
# if "波多" in search:
#     print(search.replace("波多", "*"))


#取出元组中的数字
tuple01 = ("string", "world", 1, 2, 3, 4, 6, 9, 10)
listx = []
for i in range(len(tuple01)):
    if type(tuple01[i]) == int:
        listx.append(tuple01[i])
print(listx)


#把数字取出放入总列表中
list02 =  ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
result = []
for element in list02:
    if type(element) == tuple:
        for i in element:
            result.append(i)
    elif type(element) == list:
        for i in element:
            result.append(i)
    else:
        result.append(element)
print(result)



#冒泡排序
bubble = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
for i in range(len(bubble)):
    for j in range(len(bubble)-i-1):
        if bubble[j] > bubble[j+1]:
            bubble[j],bubble[j+1] = bubble[j+1],bubble[j]
print(bubble)