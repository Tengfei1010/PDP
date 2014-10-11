#-*- coding:utf-8 -*-
import fast_powmod

DEBUG = False   # is debug mode?
def get_d_r(prime_minus_1):
    """prime_minus_1 = odd_multiplier * 2 ^ r
    返回：(odd_multiplier, r)"""
    r = 0
    bits = prime_minus_1
    while not (bits & 1):
        r += 1 # increase the r
        bits >>= 1 # right shift

    odd_multiplier = (prime_minus_1) / (2 ** r)

    if DEBUG:
        print 'r = %d, odd_multiplier = %d' % (r,odd_multiplier)
    return (odd_multiplier, r)

def fast_prime_test(prime):
    """用整除的方法先快速判断一个数是否是素数"""
    for test in xrange(3, 5000, 2):
        if prime % test == 0:
            return False# 一定不是素数
        else:
            return True # 可能是素数

def miller_rabin(prime):
    """用miller-rabin算法进行素性测试，返回：False表示一定是非素数，True则表示可能是素数"""
    witness = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    #witness = (2, 3, 5, 7, 11)
    prime_minus_1 = prime -1
    (odd_multiplier, r) = get_d_r(prime_minus_1)

    for rand_witness in witness:
        y = fast_powmod.fast_powmod(rand_witness, odd_multiplier, prime)
        if DEBUG:
            print 'y = %d'% y
        if y == 1 or y == prime-1:
            continue
        else:
            for j in range(1, r+1):
                y = fast_powmod.fast_powmod(y, 2, prime)
                if y == prime_minus_1:
                    break
                else:
                    return False# It is an absolutly composite

    return True # It maybe a prime

if __name__ == '__main__':
 prime= 40094690950920881030683735292761468389214899724061 # This is a prime number
 print '%d is Prime?\t%s' % (prime, miller_rabin(prime))
 print miller_rabin(105)# This is a composite
 print miller_rabin(2047)   # 第一个能欺骗2的数
 print miller_rabin(2047)   # 不能欺骗2、3
 print miller_rabin(1373653)# 第一个能欺骗2、3的数