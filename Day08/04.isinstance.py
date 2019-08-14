# isinstance
#2019/08/14

# a = 'hello'
# if isinstance(a,(str,tuple,int)):
#     print(True)

class Analysislog:
    def __init__(self, logPath):
        self.__path = logPath

    def getStatusCode(self):
        statusCode = {}
        with open(self.__path, 'r', encoding='utf8') as logfile:
            for lines in logfile:
                key = lines.split()[8]
                if key in ('200', '302', '304', '404', '502', '503', '504'):
                    statusCode.setdefault(key, 0)
                    statusCode[key] += 1
        return statusCode

    def getVpu(self):
        ips, info = [], 'pv: {:d} uv: {:d}'
        with open(self.__path, 'r', encoding='utf8') as logfile:
            for lines in logfile:
                ips.append(lines.split()[0])
        return info.format(len(ips), len(set(ips)))

    def getNatural(self):
        natural = {}
        with open(self.__path, 'r', encoding='utf8') as logfile:
            for lines in logfile:
                key = lines.split()[6]
                natural.setdefault(key, 0)
                natural[key] += 1
        return natural

nginxlog = Analysislog('../Day03/txtFile/access_log')
bulidFunc = dir(Analysislog)
print(bulidFunc)

if '__init__' in bulidFunc:
    print(True)
else:
    print(False)