import json

def ipsAnalysis(path):
    ips = {}
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log:
            ips.setdefault(lines.split()[0],0)
            ips[lines.split()[0]] += 1
    return ips

def codeAnalysis(path):
    code = {}
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log:
            if lines.split()[8] in ('200','301','302','400','404','405','499','502','503'):
                code.setdefault(lines.split()[8],0)
                code[lines.split()[8]] += 1
    return code

def sourceAnalysis(path):
    source = {}
    with open(file=path,mode='r',encoding='utf8') as log:
        for lines in log:
            source.setdefault(lines.split()[6],0)
            source[lines.split()[6]] += 1
    return source
