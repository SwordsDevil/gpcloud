#/usr/bin/env python3
# coding = utf-8
#
#author:SwordsDevil
#date:2019/08/07
#usage: dict opera


set01 = {1,3,2,4,5,6,3}
print(set01,type(set01))

set01.add(7)
print(set01)

set01.update((8,3,10,9))
print(set01)

set01.pop()
print(set01)
set01.remove(2)
print(set01)
set02 = {3,6,4,12,42,7}
set03 = set01 | set02
print(set03)
set04 = set01 & set02
print(set04)