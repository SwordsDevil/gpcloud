import functools
import time
import datetime


# def timeTo(func):
#     @functools.wraps(func)
#     def wrapper(*args):
#         start = time.perf_counter()
#         func(args[0])
#         end = time.perf_counter()
#
#         return 'the execute time is {:f}ms'.format((end-start)*1000)
#     return wrapper
#
# @timeTo
# def add(param):
#     a = param+ 2
#     return a
#
# print(add(10))

def timeDifference(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.perf_counter()
        func(args[0])
        end = time.perf_counter()
        return 'the time difference is {:f}ms'.format((end - start) * 1000)

    return wrapper


@timeDifference
def traverse(param):
    for i in range(param):
        print(i)

print(traverse(100))
# atime = datetime.datetime.now()
# username = ['tom','jack','marry']
# password = {'tom':'321','jack':'123','marry':'135'}
# #登录验证
# def load(func):
#     @functools.wraps(func)
#     def wrapper(*args):
#         if args[0] in username and args[1] == password[args[0]]:
#             func(args[0],args[1])
#         else:
#             print('failed!!')
#         return
#     return wrapper
#
#
# @load
# def login(user,passwd):
#     print('''
#     user:{}
#     passwd:{}
#     load once of:{}'''.format(user,passwd,atime))
#
# login('tom','321')
