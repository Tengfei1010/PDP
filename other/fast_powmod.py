#-*- coding:utf-8 -*-
__author__ = 'kevin'

def fast_powmod(a, p, n):
    """采用快速指数模方法，计算 result = a^p mod n"""
    result = a % n
    remainders = []
    while p != 1:
        remainders.append(p & 1)
        p = p >> 1
    while remainders:
        rem = remainders.pop()
        result = ((a ** rem) * result ** 2) % n
    return result