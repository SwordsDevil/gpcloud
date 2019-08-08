
import json

character = {'曹操','刘备','卧龙','孙权'}

people = {}
with open(file='../txtFile/kingdoms.txt',mode='r',encoding='utf8') as file:
    content = file.read().replace(' ','').replace('\n','')
    for character in character:
        people.setdefault(character,content.count(character))
    print(people)

# with open(file='../txtFile/threecountry.json',mode='w',encoding='utf8') as file:
#     json.dump(people,file,ensure_ascii=False)