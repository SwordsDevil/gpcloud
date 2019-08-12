import functools

#让原函数用完装饰器之后还是原函数
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('decorator this {}()'.format(func))
        func()
        print('end')
    return wrapper

@decorator
def println(parm,location):
    """
    this is println
    :param parm:
    :param location:
    :return:
    """
    print('I come from {} or {}'.format(parm,location))

print(println.__name__)
print(help(println))