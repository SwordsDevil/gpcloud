#os.walk modul
#2019/08/19

import os
import json

for dirpath,dirnames,filenames in os.walk('files'):
    print(dirpath,dirnames,filenames)

list01 = []
for dirpath,dirnames,filenames in os.walk('files'):
    dirs = ('''
    {}:
    directory:{}
    file:{}'''.format(dirpath,len(dirnames),len(filenames)))
    dirA = dirs.replace('\n','')
    list01.append(dirA)
print(list01)
with open(file='dirA',mode='w',encoding='utf8') as file:
    json.dump(list01,file,ensure_ascii=False)