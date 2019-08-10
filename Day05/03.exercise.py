import os

dirA,fileA=0,0
def dirAmount(path):
    for files in os.listdir(path):
        filesAbs = os.path.join(path,files)
        if os.path.isdir(filesAbs):
            global dirA
            dirA +=1
            dirAmount(filesAbs)
        else:
            global fileA
            fileA +=1
    return dirA,fileA

dirs,files = dirAmount(path)
print("{} directorys,{} files".format(dirs,files))

import json

def ipAmount(path):
    dict01 = {}
    with open(file=path,mode='r',encoding='uf8') as file:
        for content in file.readlines():
            ip = content.split()[0]
            if ip not in dict01.keys():
                dict01.setdefault(ip,1)
            else:
                dict01[ip] +=1
        dict01 = sorted(dict01.items(),key=lambda x: x[1],reverse=True)
        print(dict(dict01[1:10]))