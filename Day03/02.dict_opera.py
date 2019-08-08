#/usr/bin/env python3
# coding = utf-8
#
#author:SwordsDevil
#date:2019/08/07
#usage: dict opera


ipaddr = {'192.168.40.132':23,'1.32.42.32':42,'8.8.8.8':62,'1.1.1.1':32}
#查看字典键-key
for key in ipaddr.keys():
    print(key, ":",ipaddr[key])
#查看字典值-values
for vals in  ipaddr.values():
    print(vals)
print(ipaddr.values())

#查看字典键值对-元组形式
for item in ipaddr.items():
    print(item)
print(ipaddr.items())

# #增加新的键值对
# ipaddr['12.32.42.123']=32
# print(ipaddr)
# #删除指定的键值
# ipaddr.pop('1.32.42.32')
# print(ipaddr)
# #从后往前删，一次删一个键值对
# ipaddr.popitem()
# print(ipaddr)
# #清空字典
# ipaddr.clear()
# print(ipaddr)


#直接增加一个新的字典，值都为NONE
dict01 = {}.fromkeys(('tom','jack','tony'))
print(dict01)

#给字典中添加键值对
dict01.update([('tom',120),('jack',321),('cidy',213)])
print(dict01)
dict01.update([('tom',32)])
print(dict01)

dict01.setdefault('tom')
print(dict01)

