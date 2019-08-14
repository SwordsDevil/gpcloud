#coding:utf8
#2019/08/13

class Box:
    def __init__(self,length,width,high,color):
        print('init used')
        self.length = length
        self.width = width
        self.high = high
        self.color = color

    def volume(self):
        volume = self.length*self.width*self.high
        return volume

    @classmethod
    def createBox(cls,length,width,high):
        return cls(length=length,width=width,high=high,color='none')

paperBox=Box(10,15,20,'red')

ironBox = Box.createBox(10,15,20)
print(ironBox.volume())