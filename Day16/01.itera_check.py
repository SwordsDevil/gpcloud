#列表生成式
listA =[i for i in range(10)]
print(listA)

#生成器---懒人版迭代器
iterable = (i for i in range(10))
print(iterable)

#数据随取随用
for element in iterable:
    print(element)


#检查一个对象是否是迭代器
class IteraCheck:
    def __init__(self,param):
        self.param = param

    def check(self):
        try:
            iter(self.param)
            return True
        except Exception as error:
            return False,error

genetator = {1:'321','dwd':'eqwe'}
check =IteraCheck(genetator)
result = check.check()
print(result)