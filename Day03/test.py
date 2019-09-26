import json

ips={}
with open(file='./txtFile/access_log',mode='r',encoding='utf8') as log:
    for lines in log:
        ips.setdefault(lines.split()[0],0)
        ips[lines.split()[0]] += 1
    ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)
    ips = dict(ips)

# with open(file='pv.json',mode='a',encoding='utf8') as file:
#     json.dump(ips,file,ensure_ascii=False)
#     file.write('\n')

code,codes = {},['200','404','502','503']
with open(file='./txtFile/access_log',mode='r',encoding='utf8') as log:
    for lines in log:
        if lines.split()[8] in codes:
            code.setdefault(lines.split()[8],0)
            code[lines.split()[8]] +=1

# with open(file='scode.json',mode='a',encoding='utf8') as file:
#     json.dump(code,file,ensure_ascii=False)
#     file.write('\n')

source={}
with open(file='./txtFile/access_log',mode='r',encoding='utf8') as log:
    for lines in log:
        source.setdefault(lines.split()[6],0)
        source[lines.split()[6]] += 1
    source = sorted(source.items(),key=lambda x:x[1],reverse=True)
    source = dict(source[0:10])

# with open(file='source.json',mode='a',encoding='utf8') as file:
#     json.dump(source,file,ensure_ascii=False)
#     file.write('\n')

ipss = []
with open(file='./txtFile/access_log',mode='r',encoding='utf8') as log:
    for lines in log:
        ipss.append(lines.split()[0])
        pv = len(ipss)
        uv = len(set(ipss))
    print(pv,uv)


def dayu(number):
    if number[1] > 100:
        return number

iphunderd = filter(dayu,ips.items())
print(list(iphunderd))

def step(s):
    def stepS():
        nonlocal s
        s = s + 1
        return s
    return stepS
x = step(10)
print(x())