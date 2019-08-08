#!/usr/bin/env python3
#coding = utf-8

# 1.统计kingdoms.txt中"曹操"、"刘备"、"卧龙"、"孙权"各出现的次数？并将其生成字典持久化存储
# 2.统计kingdoms.txt中"青龙偃月刀"、"丈八蛇矛"、"赤兔马"、"雌雄双股剑"各出现的次数？并将其生成字典持久化存储
# 3.请将上述生成的两个字典,按照其中的出现次数进行从大到小排序？
# 4.请将上述的字典生成json格式的数据,并保存至文件中
import json

with open(file='./txtFile/kingdoms.txt',mode='r+',encoding='utf8') as file:
    content = file.read()
    print(len(content))
    c,l,w,s=0,0,0,0
    for i in range(len(content)):
        # if '曹' +'操' in (content[i] +content[i+1]):
        if '曹操' == content[i-1] + content[i]:
            c +=1
        if '刘备' == content[i-1] + content[i]:
            l += 1
        if '卧龙' == content[i-1] + content[i]:
            w += 1
        if '孙权' == content[i-1] + content[i]:
            s += 1
    # print('曹操:',c)
    # print('刘备:',l)
    # print('卧龙:',w)
    # print('孙权:',s)
    dict01={'曹操':c,'刘备':l,'卧龙':w,'孙权':s}
    print(dict01)

    q,z,ch,cx= 0,0,0,0
    for i in range(len(content)):
        if '青龙偃月刀' ==content[i-4] +content[i-3]+content[i-2]+content[i-1]+content[i]:
            q += 1
        if '丈八蛇矛' ==content[i-3] +content[i-2]+content[i-1]+ content[i]:
            z += 1
        if '赤兔马' == content[i-2] + content[i-1]+ content[i]:
            ch +=1
        if '雌雄双股剑' ==content[i-4] +content[i-3]+content[i-2]+content[i-1]+content[i]:
            cx +=1
    # print('青龙偃月刀:',q)
    # print('丈八蛇矛:',z)
    # print('赤兔马:',ch)
    # print('雌雄双股剑:',cx)
    dict02={'青龙偃月刀':q,'丈八蛇矛':z,'赤兔马':ch,'雌雄双股剑':cx}
    print(dict02)

dict03 ={}
dict03.update(dict01)
dict03.update(dict02)
list01=[]
dict_sort={}
for element in  dict03.items():
    list01.append(element[1])
list01.sort(reverse=1)
for var in list01:
    for element in dict03.items():
        if var == element[1]:
            dict_sort[element[0]] = var
print(dict_sort)


with open(file='./txtFile/package.json' ,mode='a',encoding='utf8' ) as file:
    file.write(json.dumps(dict_sort,ensure_ascii=False))
