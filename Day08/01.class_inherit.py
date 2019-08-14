
class Ball:
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius

    @classmethod
    def createBall(cls,radius):
        return cls(radius)

    def getVolume(self):
        return (4*self.PI * self.radius**3)/3

class Basketball(Ball):
    def __init__(self,radius,ui,material):
        super(Basketball,self).__init__(radius)
        self.ui = ui
        self.material = material

class football(Ball):
    def __init__(self,radius,weight):
        super(football,self).__init__(radius)
        self.weight = weight

volume = Basketball(3,'red','iron')
vBasketball = volume.getVolume()
print(vBasketball)