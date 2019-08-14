#coding:utf8
#date:2019/08/13

# class Box:
#     def __init__(self,length,width,high):
#         print('init auto operation')
#         self.length = length
#         self.width = width
#         self.high = high
#
#     def getVolume(self):
#         volume = self.length*self.width*self.high
#         return volume
#
# #通过传入属性把类实例化
# # paperBox = Box(15,20,25)
#
# #调用类中的方法
# boxVolume = Box(10,15,20).getVolume()
# print(boxVolume)



class Attach:
    VERSION = 'version is @{}'
    def __init__(self,blood,times,damage):
        self.__blood = blood
        self.times = times
        self.damage = damage

    def isLive(self):
        #调用类的常量
        print(self.VERSION.format(1.0))
        damages = self.times*self.damage
        if self.__blood > damages:
            remained = self.__blood-damages
            return 'plant is alive and remained blood is:',remained
        else:
            return 'plant is dead'

Away = Attach(70,10,8)
bloods = Away.isLive()
print(bloods)

Away.blood = 120
bloods = Away.isLive()
print(bloods)

Away.__blood = 80
print(Away.isLive())

#调用类的常量
print(Away.VERSION.format(2.0))
print(Attach.VERSION.format(2.0))