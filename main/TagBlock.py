# -*- coding: utf-8 -*- 
"""
Created on 2014年9月29日
@author: tutengfei
"""
import time
import rsa
import base64

_blocksize = 512


# noinspection PyNoneFunctionAssignment
def tag_block(pk, sk, inputfile):
    """

    :param pk:
    :param sk:
    :param inputfile:
    :return:
    """
    output = open('../file/output.txt', 'wb')
    n, g = pk
    e, d, v = sk
    with open(inputfile, 'rb') as infile:
        i = 1
        for block in rsa.varblock.yield_fixedblocks(infile, _blocksize):
            _result = str2num(_blocksize, block)
            w = gen_w(v, i)
            result = pow(g, (w + _result[0]), n)
            # print(result)
            # output.writelines((str(w) + ":" + str(result) + '\n'))
            i += 1

    output.close()


def gen_w(v, i):
    v_binary = bin(v)[2:]
    i_binary = bin(i)[2:]
    return int(v_binary + i_binary, 2)


def str2num(nbits, message):
    """
    字符转换成数字
    :param nbits:
    :param message:
    :return:
    """
    if nbits % 2 == 0:
        nbits -= 2
    else:
        nbits -= 1

    message_b64 = base64.b64encode(message)
    message_number = []

    for char in message_b64:
        message_number.append(str(ord(char)-30))
        message_str = ''.join(message_number)

    result = []
    while True:
        if len(message_str) > nbits:
            result.append(long(message_str[:nbits]))
            message_str = message_str[nbits:]
        else:
            result.append(long(message_str))
            return result


def main():
    pass
    
if __name__ == "__main__":

    import KeyGen
    start = time.time()
    pk, sk = KeyGen.keygen()
    tag_block(pk, sk, '../file/test.txt')
    end = time.time()
    print("process cost %s" % (end - start))
