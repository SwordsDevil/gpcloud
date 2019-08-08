import json

with open(file='../txtFile/access_log',mode='r',encoding='utf8') as file:
    source = {}
    for re in file.readlines():
        content = re.split()[6]
        if content not in source.keys():
            source.setdefault(content,1)
        else:
            source[content] +=1
    source = sorted(source.items(),key=lambda x:x[1],reverse=True)
    source_ten = dict(source[0:10])
    print(source_ten)