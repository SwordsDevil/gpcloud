import time
import functools
def setInterval(func):
    @functools.wraps(func)
    def wrapper(a,b):
        while True:
            time.sleep(1)
            func(a,b)
            a +=b
            if a>100:
                break
    return wrapper


@setInterval
def add(a,b):
    print(a)
add(1,2)

