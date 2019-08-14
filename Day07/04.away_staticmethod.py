#coding:utf8
#date:2019/08/13



class Box:
    def __init__(self,length,width,high):
        self.length = length
        self.width = width
        self.high = high

    @staticmethod
    def explain(*args,**kwargs):
        print('''
        Thanks you use Box class.
        please input Box's length,width,high
        {}
        {}
        '''.format(args[0],args[1]))

Box.explain('copyright@2019','version 3.0')
