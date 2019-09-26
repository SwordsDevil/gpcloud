# erro dispose
#2019/08/16


try:

    var01 ,var02 = 'hello',18
    print(var01+var02)
    print(1/0)
except Exception as erro:
    print('[ERRO]:{}'.format(erro))
finally:
    pass

print('go on..')


class CpuError(Exception):
    pass

try:
    string = input('please input :')
    raise CpuError('cpu info error')
except Exception as error:
    print('[ERROR]:{}'.format(error))
finally:
    pass
