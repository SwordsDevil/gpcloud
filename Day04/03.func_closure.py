#闭包
def closure(x):
    def close(y):
        return y*x
    return close

result = closure(3) #result = close
print(result(3))