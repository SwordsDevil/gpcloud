#random code check
#2019/08/20

import random

# number = random.random()
# print(number)
#
# number2 = random.uniform(1,20)
# print('随机数为：{:.2f}'.format(number2))
#
# number = random.randint(10,30)
# print(number)
#
# listA = [1,2,5,9,32]
# element = random.choice(listA)
# print(element,type(element))
#
# random.shuffle(listA)
# print(listA)


#嵌套函数产生验证码
# def createcode(n):
#     if n <= 0:
#         return 'lose!'
#     def wrap(n):
#         codes = ''
#         for i in range(n):
#             code = [str(random.randint(0,9)),chr(random.randint(65,90))]
#             codes += random.choice(code)
#         return codes
#     return wrap(n)
#
# codes = createcode(4)
# print('验证为：{}'.format(codes))
# input = input('请输入验证码：')
# if input.lower() == codes.lower():
#     print('输入正确')
# else:
#     print('输入错误')


#xjb自建
def makeCode(n):
    if n<=0:
        print('false')
    code=''
    for i in range(n):
        number = [str(random.randint(0,9)),chr(random.randint(65,90))]
        code += random.choice(number)
    return code
codes = makeCode(4)
print('codes is {}'.format(codes))
pcode = input('请输入验证码：')
if pcode.upper() == codes.upper():
    print('commit true')
else:
    print('input error')
