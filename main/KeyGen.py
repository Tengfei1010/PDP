# -*- coding: utf-8 -*- 
'''
Created on 2014年9月29日

@author: tutengfei
'''
import rsa
import Euclid
from time import clock as now   #记时模块

begin = now()   #记时开始

def gen_p_q(nbits=512):
    ''' generate KEYGEN  pk  of  N  '''
    p = rsa.prime.getprime(nbits)

    q = rsa.prime.getprime(nbits)

    return (p , q)


def g_f(a,n):
    ''' return gcd ( a+- 1 / n )'''
    if rsa.prime.gcd(a-1, n) or rsa.prime.gcd(a+1,n):
        return True
    return False


def gen_g(n):
    ''' generate KEYGEN pk of g'''
    while True:
        a = rsa.randnum.randint(n-1)
        if rsa.prime.are_relatively_prime(n, a):
            if g_f(a,n):
                return a*a
            
def gen_n_g(p, q):
    N = p * q
    g = gen_g(N)
    
    return (N,g)


    
            
def gen_m(p, q):
    p1 = p -1
    q1 = q -1
    
    m = p1 * q1 / 4
    
    return m
    

def gen_e_d(m):
    """产生(e, d); m is p1 * q1"""
    # Generate a number e so that gcd(e, m) = 1, start with e = 3
    e = 3
    while True:
        d = Euclid.extended_Euclid(e, m)
        if Euclid.gcd(m, e) == 1 and d > 0:
            break
        else:
            e += 2
    return (e, d)

def gen_pk(p,q):
    (N,g) = gen_n_g(p, q)
    return (N,g)
    
    
    
def gen_sk(p, q):
    m = gen_m(p, q)
    (e,d) = gen_e_d(m)
    v = rsa.randnum.randint(1000)
    
    return (e,d,v)


def KeyGen():
    (p,q) = gen_p_q()
    pk = gen_pk(p, q)
    sk = gen_sk(p, q)
    
    return (pk,sk)

if __name__=='__main__':
    begin = now()   #记时开始
    (pk,sk)=KeyGen()
    print (pk)
    print (sk)
    end = now()
    print(end - begin)
    
    
    
    


    
           

          





