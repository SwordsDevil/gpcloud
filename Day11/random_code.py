#random code check
#2019/08/20

import random

number = random.random()
print(number)

number2 = random.uniform(1,20)
print('随机数为：{:.2f}'.format(number2))

number = random.randint(10,30)
print(number)

listA = [1,2,5,9,32]
element = random.choice(listA)
print(element)

random.shuffle(listA)
print(listA)



def createcode(n):
    if n <= 0:
        return 'lose!'
    def wrap(n):
        codes = ''
        for i in range(n):
            code = [str(random.randint(0,9)),chr(random.randint(65,90))]
            codes += random.choice(code)
        return codes
    return wrap(n)

codes = createcode(4)
print('验证为：{}'.format(codes))
input = input('请输入验证码：')
if input.lower() == codes.lower():
    print('输入正确')
else:
    print('输入错误')