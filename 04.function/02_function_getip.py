#!/usr/bin/env python3
#coding:utf8


import json

def getIp(path):
    ips = {}
    with open(file=path,mode='r',encoding='utf8') as file:
        for content in file.readlines():
            ip = content.split()[0]
            if ip not in ips:
                ips.setdefault(ip,1)
            else:
                ips[ip] +=1
        ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)
        return ips
    #print(ips[0:10])


print(getIp('../Day03/txtFile/access_log'))