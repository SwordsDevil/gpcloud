#package property
#2019/08/14

# class Box:
#     def __init__(self,length,width,high):
#         self.__length = length
#         self.__width = width
#         self.__high = high
#     @classmethod
#     def createBox(cls,legnth,width,high):
#         return cls(legnth,width,high)
#
#     @property
#     def getArea(self):
#         sideArea = self.__length*self.__high + self.__width*self.__high
#         lowArea = self.__length*self.__width
#         return (sideArea+lowArea)*2
#
#     @getArea.setter
#     def getArea(self,tail):
#         self.__length,self.__width,self.__high = tail
#
#     @getArea.deleter
#     def getArea(self):
#         print('this attribute be deleted!')
#
#     def getVolume(self):
#         return self.__length*self.__width*self.__high
#
# paperBox = Box.createBox(10,15,20)
# print(paperBox.getArea)
#
# paperBox.getArea = 5,10,15
# print(paperBox.getArea)

# del paperBox.getArea

class Attach:
    def __init__(self,blood,times,damage):
        self.__blood = blood
        self.__times = times
        self.damage = damage
    @classmethod
    def creatAttach(cls,blood,times,damages):
        return cls(blood,times,damages)

    @property
    def isLive(self):
        damages = self.__times*self.damage
        if self.__blood > damages:
            remaind = self.__blood - damages
            return "is still alive the blood is:{}".format(remaind)
        else:
            return "is dead!"

    @isLive.setter
    def isLive(self,tail):
        self.__blood,self.__times,self.damage = tail

    @isLive.deleter
    def isLive(self):
        print('the attribute be delete')


monster = Attach.creatAttach(100,10,7.5)
print(monster.isLive)

monster.isLive = 120,12,8
print(monster.isLive)