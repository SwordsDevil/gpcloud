#/usr/bin/env python3
# coding = utf-8
#
#author:SwordsDevil
#date:2019/08/07
#usage: dict opera

ips = {'192.168.161.10':23,'192.168.40.140':130, '1.1.1.1': 85, '8.8.8.8': 102}

# 方式一：冒泡排序
# ips_sort =[]
# for item in ips.items():
#     ips_sort.append(item)
# print(ips_sort)
# for i in range(len(ips_sort)):
#     for j in range(len(ips_sort)-i-1):
#         if ips_sort[j][1] > ips_sort[j+1][1]:
#             ips_sort[j],ips_sort[j+1] = ips_sort[j+1],ips_sort[j]
# ips_sort = dict(ips_sort)
# print(ips_sort)

#方式二：国盛法
list01 = []
dict01 = {}
for item in ips.items():
    list01.append(item[1])
list01.sort(reverse=1)
for var in list01:
    for item in ips.items():
        if var == item[1]:
            dict01[item[0]] = var
dict01 = dict(dict01)
print(dict01)