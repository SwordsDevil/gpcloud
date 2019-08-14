import functools
import datetime

#登录验证函数
username = ['tom','jack','cindy']
password = {'tom':'!@#123','jack':'!@#123','cindy':'123!@#'}

# def load(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         if args[0] in username and args[1] == password[args[0]]:
#             func(args[0],args[1])
#         else:
#             print('filed!!!')
#     return wrapper
#
# atime = datetime.datetime.now()
#
# @load
# def login(user,passwd):
#     print('''
#     user:{}
#     passwd:{}
#     load once of:{}'''.format(user,passwd,atime))

# login('tom','!@#123')
def load(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if args[0] in username and args[1] == password[args[0]]:
            print('this is load success')
            func(args[0],args[1])
        else:
            print('load failed!!')
    return wrapper

atime = datetime.datetime.now()
@load
def login(user,passwd):
    print('''
    user:{}
    passwd:{}
    load once of {}'''.format(user,passwd,atime))

login('tom','!@#123')