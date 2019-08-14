import os

a = os.listdir('H:\pycharm_Project\gpcloud.git')
print(a)

b= os.getcwd()
print(b,type(b))

#c = os.chdir('H:\pycharm_Projiect\gpcloud.git')

d = os.path.isdir('H:\pycharm_Project\gpcloud.git\Day04')
print(d)

e = os.path.isfile('H:\pycharm_Project\gpcloud.git\Day05\exam.py')
print(e)

f = os.path.exists('H:\pycharm_Project')
print(f)

g = os.path.getsize('H:\Download\\typora-setup-x64.exe')
print("{:.3f}".format(g/1024/1024))

h = os.path.abspath('01.os_func.py')
print(h)

i = os.path.split('H:\Download\\typora-setup-x64.exe')
print(i)
i  = os.path.splitext('typora_set_x64.exe')
print(i)

j = os.path.join('H:\Download','01.0s_func.py')
print(j)

file = os.path.basename('H:\Download')
print(file)

dir = os.path.dirname('H:\Download')
print(dir)

dirA,fileA = 0,0
def dirAmount(path):
    for files in os.listdir(path):
        fileAbs = os.path.join(path,files)
        if os.path.isdir(fileAbs):
            global dirA
            dirA += 1
            dirAmount(fileAbs)
        else:
            global fileA
            fileA += 1
    return '{} director,{} files'.format(dirA,fileA)
    # return dirA,fileA
dirs = dirAmount('H:\pycharm_Project\gpcloud')
print(dirs)