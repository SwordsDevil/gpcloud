
import json

ips = {}
with open(file='../txtFile/access_log',mode='r',encoding='utf8') as file:
    for content in file.readlines():
        ip = content.split()[0]
        if ip not in ips.keys():
            ips.setdefault(ip,1)
        else:
            ips[ip] +=1
ips = sorted(ips.items(),key=lambda x: x[1],reverse=True)
ips = dict(ips[0:10])
print(ips)

# with open(file='../txtFile/threecountry.json',mode='a',encoding='utf8') as log:
#     log.write('\n')
    # json.dump(ips,log,ensure_ascii=False)

