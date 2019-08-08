#!/usr/bin/env python3
#coding=utf8

# 5.请统计access_log中访问量前十的IP地址,并生成json格式数据,保存至文件中.(用python代码实现)
import json
with open(file='./txtFile/access_log',mode='r+',encoding='utf8') as file:
    content = file.readlines()
ips,dict_ip = [],{}
for element in content:
    ip = element.split()[0]
    ips.append(ip)
ips_set = set(ips)

for ipp in ips_set:
    ip_number = ips.count(ipp)
    dict_ip[ipp] = ip_number



list_number = []
dict_sort_ip = {}
for i in dict_ip.items():
    list_number.append(i[1])
#print(list_number)
list_number.sort(reverse=1)
#print(list_number)

list_ten=list_number[0:10]
print(list_ten)

for var in list_ten:
    for element in dict_ip.items():
        if var == element[1]:
            dict_sort_ip[element[0]]=var
print(dict_sort_ip)

with open(file='./txtFile/package.json',mode='a',encoding='utf8') as file:
    file.write(json.dumps(dict_sort_ip,ensure_ascii=False))




