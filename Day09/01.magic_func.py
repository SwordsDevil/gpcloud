# magic function
#2019/08/15

# class Ball:
#     #相当于换了一种声明类的方式，创造一个固定的内存空间，把实例化的对象都存在这个空间中，节约了内存
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     #实例化的时候被调用
#     def __init__(self,radius):
#         print('__init__ be called')
#         self.__radius = radius
#
#     #让实例化的对象可以像函数那样被调用，可以随意的修改属性和私有属性的值
#     def __call__(self, radius):
#         self.__radius = radius
#
#     #实例回收是被调用，就是被删除的时候，python有自动回收机制，用完了就会回收
#     def __del__(self):
#         print('instance is deleted')
#
#     #当实例化的对象被打印的时候，这个函数就被执行
#     def __str__(self):
#         print('__str__ be called')
#
#     def getVolume(self):
#         return (4*3.14*self.__radius**3)/3？



class Ball:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,radius):
        print('__init__ called')
        self.__radius = radius

    def __call__(self, *args, **kwargs):
        self.__radius = args[0]


    def __del__(self):
        print('object deleted')

    def __str__(self):
        return '打印了对象'

    def getVolume(self):
        return (4*3.14*self.__radius**3)/3


ironball = Ball(12.3)
print(ironball.getVolume())
ironball(10)
# ironball.radius = 10
print(ironball.getVolume())
# wooldenball = Ball(10)
# print(ironball)
# print('ironball    id {}'.format(id(ironball)))
# print('wooldenball id {}'.format(id(wooldenball)))

