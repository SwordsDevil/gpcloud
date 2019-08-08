import json
code_amount = {}
number_list = ['200','404','502','503']
with open(file='../txtFile/access_log',mode='r',encoding='utf8') as file:

    for content in file.readlines():
        code = content.split()[8]
        if code not in code_amount.keys():
            code_amount.setdefault(code,1)
        else:
            code_amount[code] += 1
    code_amount = dict(sorted(code_amount.items(),key=lambda x:x[1],reverse=True))
    print(code_amount)
    for item in list(code_amount):
        #print(item)
        if item not in number_list:
            code_amount.pop(item)
    print(code_amount)

