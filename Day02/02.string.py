#!/usr/bin/env python3
#coding = utf-8
#
#author: SwordsDevil
#date:2019/08/06
#usage:string


string01 = 'hello chenwenbin'
print(string01)

string02 = "i'm 18 years old"
print(string02)

#格式化打印（带有格式的打印）--format
string03 = '''System monitor messages:
            CPU rate: {}
            MEN rate: {}
            DISK rate: {}
            NETWORK mbps: {}
        @{}'''.format("80%","70%","60%","1000M","chenwenbin")
print(string03)