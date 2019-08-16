#diamond inherit
#2019/08/15

class A:
    def __init__(self,**kwargs):
        print('A')


class B(A):
    def __init__(self,**kwargs):
        print('B')
        super(B,self).__init__()

class C(A):
    def __init__(self,**kwargs):
        print('C')
        super(C, self).__init__()


class D(C,B):
    def __init__(self,**kwargs):
        print('D')
        super(D, self).__init__()
        self.kwargs = kwargs

person = D(name='chenwenbin',age=18,sex='man',high='180',width='20')
