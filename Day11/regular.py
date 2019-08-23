#regular
#2019/08/19

import re

data = 'Last login: Thu Mar  2 10:04:52 2019 from 39.100.110.135'
Date = re.split('[:.]',data)
print(Date)


data = '39.200.110.135 [ERROR]: no such file or directory.'
result = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',data)
print(result)

data = 'abc Abc aBc'
pattern = re.compile('a.c')
result = pattern.search(data)
print(result)


data = 'abc DCB aDc'
result = pattern.sub(repl='4321',string=data,count=1)
print(result)