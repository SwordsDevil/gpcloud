import json
#
# ips = {}
# with open(file='access.log',mode='r',encoding='utf8') as file:
#     for content in file.readline():
#         ip = content.split()[0]
#         if ip not in ips.keys():
#             ips.setdefault(ip,1)
#         else:
#             ips[ip] +=1
#     ips = sorted(ips.items(),key=lambda x: x[1],reverse=True)
#     ips = dict(ips[0:10])
#
# with open(file='pv.json',mode='w',encoding='utf8') as file:
#     json.dump(ips,file,ensure_ascii=False)



# import json
# codes = {}
# list_code = ['200','404','502','503']
# with open(file='access.log',mode='r',encoding='utf8') as file:
#     for content in file.readline():
#         ip = content.split()[8]
#         if ip not in codes.keys():
#             codes.setdefault(ip,1)
#         else:
#             codes[ip] +=1
#     codes = sorted(codes.items(),key=lambda x: x[1],reverse=True)
#
#     for element in list(codes):
#         if element not in list_code:
#             codes.pop(element)
#     print(codes)
#
# with open(file='scode.json',mode='w',encoding='utf8') as file:
#     json.dump(codes,file,ensure_ascii=False)


# import json
# source = {}
# with open(file='access.log',mode='r',encoding='utf8') as file:
#     for content in file.readline():
#         re = content.split()[6]
#         if re not in source.keys():
#             source.setdefault(re,1)
#         else:
#             source[re] +=1
#     source = sorted(source.items(),key=lambda x: x[1],reverse=True)
#     source = dict(source[0:10])
#
# with open(file='ipaddr.json',mode='w',encoding='utf8') as file:
#     json.dump(source,file,ensure_ascii=False)


# ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}
# ips = dict(sorted(ips.items(),key=lambda x:x[1],reverse=True))
# print(ips)


# def anlyze(path):
#     pvs = []
#     with open(file=path,mode='r',encoding='utf8') as file:
#         for content in file.readlines():
#             pv = content.split()[0]
#             pvs.append(pv)
#         pvss = len(pvs)
#         uvs = list(set(pvs))
#         uvs = len(uvs)
#         return pvss,uvs
#
# pv,uv = anlyze('../Day03/txtFile/access_log')
# print(pv,uv)

import json

ips = {}
with open(file='../Day03/txtFile/access_log',mode='r',encoding='utf8') as file:
    for content in file.readlines():
        ip = content.split()[0]
        ips.setdefault(ip,0)
        ips[ip] += 1
ips = dict(sorted(ips.items(),key=lambda x: x[1],reverse=True))
# print(ips)

# def ipAddr(element):
#     if element[1] > 100:
#         return ips
# ips_list = ips.items()
# ips_hunderd = filter(ipAddr,ips_list)
# print(list(ips_hunderd))
def ipsHunderd(element):
    if element[1] > 100:
        return ips

listA = filter(ipsHunderd,ips.items())
print(list(listA))



# def stepCound(step):
#     print('请输入步数：{}'.format(step))
#     def stepS():
#         nonlocal step
#         step +=1
#         return step
#     return stepS
#
# opera = stepCound(10)
# print(opera())
