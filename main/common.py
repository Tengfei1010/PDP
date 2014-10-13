import base64

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


def permutation(number):
    """
    block tag index permutation
    :param number: integer
    :return: permutation number
    """
    str = bin(number)[2:]
    length = len(str)
    if not length % 8 == 0:
        t = length / 8
        length = 8 * (t + 1)
        str = b'0' * (length - len(str)) + str
    t_str = str[(length / 2) + 1:] + str[:(length / 2) + 1]
    return int(t_str, 2)


def gen_indices(key, number, mod=500):
    return (permutation(number) * key) % mod


def gen_coefficients(key, number, mod=100):
    return permutation(permutation(number) * key) % mod