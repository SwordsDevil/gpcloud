import json

person = {'曹操','刘备','卧龙','孙权','青龙偃月刀','丈八蛇矛','赤兔马','双股剑'}
def personNumber(path):
    person_arms= {}
    with open(file=path,mode='r',encoding='utf8') as file:
        content = file.read().replace(' ','').replace('\n','')
        for element in person:
            person_arms.setdefault(element,content.count(element))
        person_arms = dict(sorted(person_arms.items(), key=lambda x: x[1], reverse=True))
        print(person_arms)


#personNumber('../txtFile/kingdoms.txt')
