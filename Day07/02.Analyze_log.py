#coding:utf8
#2019/08/31

class AnalyzeLog:
    def __init__(self,path):
        self.path = path

    def getPvUv(self):
        ips = []
        with open(self.path, 'r', encoding='utf8') as logfile:
            for lines in logfile:
                ips.append(lines.split()[0])
        pv = len(ips)
        uv = len(set(ips))
        return pv,uv

    def getStatusCode(self):
        statusCode = {}
        with open(self.path, 'r', encoding='utf8') as logfile:
            for lines in logfile:
                key = lines.split()[8]
                if key in ('200', '302', '304', '404', '502', '503', '504'):
                    statusCode.setdefault(key, 0)
                    statusCode[key] += 1
        return statusCode

    def hotNatural(self):
        natural = {}
        with open(self.path, 'r', encoding='utf8') as logfile:
            for lines in logfile:
                key = lines.split()[6]
                natural.setdefault(key, 0)
                natural[key] += 1
        return natural

logpath = AnalyzeLog('../Day03/txtFile/access_log')
print(logpath.getPvUv())
print(logpath.getStatusCode())
print(logpath.hotNatural())



