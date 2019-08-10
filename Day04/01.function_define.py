#!/usr/bin/env python3
#coding:utf8
#
#author:SwordsDevil
#date: 2019/08/08
#usage:functions define


def funName(a,b,c):
    """
    function max
    :param a: int
    :param b: int
    :param c: int
    :return: a
    """
    if a < b  and b > c:
        a,b = b,a
    elif a< c  and c > b:
        a,c = c,a
    return a
print(funName(1,2,3))
