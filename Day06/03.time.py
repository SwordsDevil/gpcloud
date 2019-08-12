import time
import datetime
import functools

#打印系统时间
atime = datetime.datetime.now()
print(atime)
# print(atime.second)

#计算函数的执行时间（时间差）
def executeTime(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        first = time.perf_counter()
        func(*args,**kwargs)
        end = time.perf_counter()
        print('{}的执行时间:{:f}ms'.format(func.__name__,(end-first)*1000))
    return wrapper

@executeTime
def createList(param):
    a = param+2
    return a

# print(createList(1000))
createList(100)