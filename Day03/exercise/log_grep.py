import json

def getIp(path):
    ips = {}
    with open(file=path,mode='r',encoding='utf8') as file:
        for content in file.readlines():
            ip = content.split()[0]
            if ip not in ips.keys():
                ips.setdefault(ip,1)
            else:
                ips[ip] += 1
        ips = sorted(ips.items(),key=lambda x:x[1],reverse=True)
        ips = dict(ips[0:10])
        print(ips)
getIp('../txtFile/access_log')

def getCode(path):
    codes = {}
    code_number = ['200','404','502','503']
    with open(file=path,mode='r',encoding='utf8') as file:
        for content in file.readlines():
            code = content.split()[8]
            if code not in codes.keys():
                codes.setdefault(code,1)
            else:
                codes[code] +=1
        codes = dict(sorted(codes.items(),key=lambda x:x[1],reverse=True))
        #删除没有的状态码
        for element in list(codes):
            if element not in code_number:
                codes.pop(element)
        print(codes)
        #选出有的状态码
        # codes_some = {}
        # for element in codes.keys():
        #     if element in code_number:
        #         codes_some[element] = codes[element]
        # print(codes_some)
getCode('../txtFile/access_log')

def getResource(path):
    sources = {}
    with open(file=path,mode='r',encoding='utf8') as file:
        for content in file.readlines():
           source = content.split()[6]
           if source not in sources.keys():
               sources.setdefault(source,1)
           else:
               sources[source] +=1
        sources = sorted(sources.items(),key=lambda x:x[1],reverse=True)
        sources = dict(sources[0:10])
        print(sources)
getResource('../txtFile/access_log')