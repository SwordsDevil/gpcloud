#!/usr/bin/env python3
#coding:utf8

import time
import pymysql


date = time.strftime('%Y%m%d%H%M%S',time.localtime())

def PUv(path):
    ips = []
    with open(file=path,mode='r',encoding='utf8') as file:
        for lines in file:
            ips.append(lines.split()[0])
    Pv = len(ips)
    Uv = len(set(ips))
    return Pv,Uv
Pv,Uv = PUv('access_log')

def Topip(path):
    ips = {}
    with open(file=path,mode='r',encoding='utf8') as file:
        for lines in file:
            ips.setdefault(lines.split()[0],0)
            ips[lines.split()[0]] +=1
        ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)
        ips = ips[0:10]
    return ips
ips = Topip('access_log')
ips1 = (str(ips[0][0])+'-'+str(ips[0][1]))
print(type(ips1),ips1)
# print(ips)
def Code(path):
    code= {}
    with open(file=path,mode='r',encoding='utf8') as file:
        for lines in file:
            key = lines.split()[8]
            for i in ('200', '302', '304', '404', '502', '503', '504'):
                code.setdefault(i,0)
            if key in ('200', '302', '304', '404', '502', '503', '504'):
                code[key] +=1
    # codeAmount= [element[1] for element in code.items()]
    return code
code = Code('access_log')
# print(code)
# for i in code.items():
#     print(i[0])
# client = pymysql.connect(
#     host='192.168.40.143',
#     port=3306,
#     user='Swords',
#     password='(Swords..0908)',
#     db='webInfo',
#     charset='utf8'
# )
# cursors = client.cursor()
# puv = "insert into PUv values({},{},{})"
# cursors.execute(puv.format(date,Pv,Uv))
# codes = "insert into code values({},{},{},{},{},{},{},{})"
# cursors.execute(codes.format(date,code[0],code[1],code[2],code[3],code[4],code[5],code[6]))
# ip = "insert into IpTop values({},'{}',{},'{}',{},'{}',{})"
# cursors.execute(ip.format(date,ips[0][0],ips[0][1],ips[1][0],ips[1][1],ips[2][0],ips[2][1]))
#
# client.commit()
# client.close()