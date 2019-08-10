import os

dictA = fileA = 0
def dirCount(path):
    for files in os.listdir(path):
        fileAbs = os.path.join(path,files)
        if os.path.isdir(fileAbs):
            global dictA
            dictA +=1
            dirCount(fileAbs)
        else:
            global fileA
            fileA +=1
    return dictA,fileA

dicts ,files = dirCount('D:apache-jmeter-5.1')

print("{} directers,{} files".format(dicts,files))