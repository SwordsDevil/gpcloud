
def decorator(func):
    def wrappers(*args,**kwargs):
        print("执行了装饰器")
        func()
        print('执行完了装饰器')
    return wrappers

@decorator
def println():
    print('hello world')

println()


users = ['tom','jerry','jack']
password = {'tom':'123','jerry':'321','jack':'123'}

def decorator(func):
    def wrapper(user,passwd):
        if user in users and password[user] == passwd :
            print('decorator execute')
            func(user,passwd)
        else:
            print("faild!!!")
    return wrapper

@decorator
def login(user,passwd):
    print('登录界面')

@decorator
def check(user,passwd):
    print('验证界面')

page = input('请输入要进入的页面：')
u = input('请输入用户名：')
p = input('请输入密码：')

if page == 'login':
    login(u,p)
elif page == 'check':
    check(u,p)
else:
    print('没有这个页面')