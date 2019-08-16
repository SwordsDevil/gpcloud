#chain inherit
#2019/08/15

class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class B(A):
    def __init__(self,name,age,sex):
        super(B,self).__init__(name,age)
        self.sex = sex

class C(B):
    def __init__(self,name,age,sex,high):
        super(C, self).__init__(name,age,sex)
        self.high = high

class D(C):
    def __init__(self,name,age,sex,high,weight):
        super(D,self).__init__(name,age,sex,high)
        self.weight = weight

person = D(name='chenwenbin',age=18,sex='man',high='180',weight='55')
