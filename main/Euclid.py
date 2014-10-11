#-*- coding:utf-8 -*-
__author__ = 'kevin'
# a should be greater than b
def gcd (a, b):
    """Compute GCD(greatest common divisor) of two numbers
    求两个数的最大公约数"""
    #print 'a =%d b= %d' % (a, b)
    if a < b:
        (a, b) = (b, a) #交换a和b
    if b == 0:
        return a  #返回
    else:
        return gcd(b, a % b) #递归调用程序本身

def extended_Euclid(e, z):
    """利用扩展的欧几里德(extended Euclid)算法来求密钥e的模Z乘法逆元
    公式：d*e = 1 mod Z
    已知：e, Z，求e的mod Z的乘法逆元
    返回: d = e^(-1) mod Z"""
    (x1, x2, x3) = (1, 0, z)
    (y1, y2, y3) = (0, 1, e)
    while True:
        if y3 == 0:
            return False
        if y3 == 1:
            return y2
        div = x3 / y3
        (t1, t2, t3) = (x1 -div*y1, x2 - div*y2, x3 - div*y3)
        (x1, x2, x3) = (y1, y2, y3)
        (y1, y2, y3) = (t1, t2, t3)

if __name__ == '__main__':
    print gcd(7,261)
    print extended_Euclid(7, 216)

#求大数的模n的乘法逆元，用的方法是扩展的欧几里得算法。
