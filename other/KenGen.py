#-*- coding:utf-8 -*-
#系统模块
import math #数学模块
import random   #随机数模块
from time import clock as now   #记时模块

#自定义模块
import Euclid
import fast_powmod
import prime_test
#import encode


DEBUG = True   #调试模式
begin = now()   #记时开始

def produce_primes(decimal_bits):
    """产生指定位数的随机素数"""
    begin = 10 ** (decimal_bits -1) + 1 # like: 1000000000000000001
    end = 10 ** (decimal_bits + 1) - 1  # like: 99999999999999999999

    while True:
        random.seed()
        #产生一个指定范围的随机奇数（伪随机数）
        odd = random.randrange(begin, end, 2)
        print("随机产生的素数----",odd)
        #先用快速法判断一下，如果不是素数，则重新产生一个奇数
        if prime_test.fast_prime_test(odd) == False:
            continue
        #对奇数的素性测试
        is_prime = prime_test.miller_rabin(odd)
        if is_prime == True:
            return odd
        elif is_prime == False:
            continue

binary_bits = 1024  #设置n 的二进制位数
decimal_bits = int(math.ceil(binary_bits * math.log10(2))) #n的十进制位数
decimal_bits >>= 1  # decimal_bits / 2

if DEBUG:
    print 'n的十进制位数为：', decimal_bits

def produce_p_q():
    """产生p和q"""
    # produce
    p = produce_primes(decimal_bits)
    # produce q, q should not equal to p
    while True:
        q = produce_primes(decimal_bits)
    if q != p:
        return (p, q)
(p, q) = produce_p_q()
n = p * q

print("N is :",n)
def bits_of_n(n):
    """计算最后产生的n的二进制位数"""
    bits = 0
    while n > 1:
        n >>= 1
        bits += 1
    return bits
bits = bits_of_n(n)
print 'The bits of n is:',bits
m = (p-1) * (q-1)
def produce_e_d():
    """产生(e, d)"""
    # Generate a number e so that gcd(e, m) = 1, start with e = 3
    e = 3
    while True:
        d = Euclid.extended_Euclid(e, m)
        if Euclid.gcd(m, e) == 1 and d > 0:
            break
        else:
            e += 2
    return (e, d)
(e, d) = produce_e_d()
if DEBUG:
    print 'q is:', q
    print 'p is:', p
    print 'm is:', m
    print 'e is:', e
    print 'd is:', d
    print 'The private key is:', (d, n) #公钥
    print 'The public key is:', (e, n)  #私钥













'''
def encrypt(groups):
    """对数字化后的消息分组进行加密"""
    encrypted = [] #密文
    for message in groups:
        encrypted.append(fast_powmod.fast_powmod(message, e, n)) #加密
    return encrypted #返回加密后的密文分组

def decrypt(cipher):
    """对加密后的密文分组进行解密"""
    plain_text = []
    for decrypted in cipher:
        plain_text.append(fast_powmod.fast_powmod(decrypted, d, n)) # 解密
    return plain_text

#要加密的消息
message = 'I love you more than I can Say!---This message is encrypted by RSA.I love you more than I can Say!---This message is encrypted by RSA.I love you more than I can Say!---This message is encrypted by RSA.I love you more than I can Say!---This message is encrypted by RSA.'

groups = encode.str2num(decimal_bits*2, message) #将消息转化为数字化的分组

print '消息共分为%d组进行加密。' % len(groups)
cipher = encrypt(groups)# 加密
plain_text = decrypt(cipher)# 解密
#cipher = ''.join(cipher)
print 'The Cipher is:', cipher
plain_text = encode.num2str(plain_text) #将数字化分组转换成消息
#解密后的明文(应该与消息相同)
print 'The Plain_text is:', plain_text
end = now() # 记时结束
print '加密-解密过程共用时间：%f 秒！' % (end-begin)
'''
