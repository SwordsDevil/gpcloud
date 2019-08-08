import json

arms,amount = {'青龙偃月刀','丈八蛇矛','赤兔马','双股剑'},{}
with open(file='../txtFile/kingdoms.txt',mode='r',encoding='utf8') as file:
    content = file.read().replace(' ','').replace('\n','')
    for arms in arms:
        amount .setdefault(arms,content.count(arms))
    print(amount)

with open(file='../txtFile/threecountry.json',mode='a',encoding='utf8') as file:
    file.write('\n')
    json.dump(amount,file,ensure_ascii=False)
