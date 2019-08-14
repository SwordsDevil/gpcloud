#packaging
#2019/08/14

class Ball:
    PI = 3.14
    def __init__(self,radius):
        self.__radius = radius

    @classmethod
    def createBall(cls,radius):
        return cls(radius)

    def getVolume(self):
        return (4*self.PI*self.__radius**3)/3

basketball = Ball.createBall(12.3)
print(basketball.getVolume())

basketball.radius = 20
print(basketball.getVolume())

# basketball = Ball(12.3)
# print(basketball.getVolume())
#
# basketball.raduis = 10
# print(basketball.getVolume())
