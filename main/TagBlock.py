# -*- coding: utf-8 -*- 
'''
Created on 2014年9月29日

@author: tutengfei
'''
import rsa

_blocksize = 2048
def tagBlock(pk,sk,inputfile):
    
    (N, g) = pk
    (e, d, v) = sk
    count = 0
    with open(inputfile,'rb') as infile:
        for block in rsa.varblock.yield_fixedblocks(infile, _blocksize):
            w = str((bin(v)[2:])) + str((bin(count)[2:]))
            count = count + 1
            # h function is for h(w)-> QRn
            h_w = int(w, 2)
            _result = gen_binary(block)
            print _result 
            
            
            
def gen_binary(string):
    with open ('../file/output.txt','wb') as output:
        for i in string:
            temp = (bin(ord(i))[2:])
            temp = '0' * (8-len(temp)) + temp
            output.write(temp)
            
    
if __name__ =="__main__":
    import KeyGen
    (pk,sk) = KeyGen.KeyGen()
    tagBlock(pk, sk, '../file/test.txt')
    
    
    
    
