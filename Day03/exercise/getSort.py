
import json

get_sort = []
with open(file='../txtFile/threecountry.json',mode='r',encoding='utf8') as file:
    for line in file.readlines():
        content = json.loads(line)
        get_sort.append(dict(sorted(content.items(), key=lambda x: x[1], reverse=True)))
    print(get_sort)

# with open(file='../txtFile/threecountry.json',mode='a',encoding='utf8') as file:
#     file.write('\n')
#     json.dump(get_sort,file,ensure_ascii=False)


