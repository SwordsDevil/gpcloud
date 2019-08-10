
def func01(element):
    return element**2

list01 = [1,2,3,4]
n = map(func01,list01)
print(list(n))

def filt(element):
    if element % 2 == 0:
        return element

list02 = [23,42,42,3,3112,313,412,23,5,6763,7342,873,387,4235,342]
m = filter(filt,list02)
print(list(m))


from functools import reduce

def re(a,b):
    return a*b

number = [1,2,4,6,5]
mutiply = reduce(re,number)
print(mutiply)