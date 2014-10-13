__author__ = 'kevin'

_blocksize = 512

import rsa

def gen_proof(pk, chal):
    n, g = pk
    c, k1, k2, s = chal
    block_size = count_file_blocks('../file/test.txt')
    indices = []
    coefficients = []
    for j in range(c):
        indices.append()
        coefficients.append(permutation(permutation(j) * k2))


def gen_indices(key, number):
    return permutation(number) * key


def gen_coefficients(key, number):
    return permutation(permutation(number) * key)


def gen_w(v, i):
    v_binary = bin(v)[2:]
    i_binary = bin(i)[2:]
    return int(v_binary + i_binary, 2)


def count_file_blocks(input_file):
    """
    count blocks of challenge files
    :param input_file:
    :return: the count of blocks
    """
    count = 0
    with open(input_file, 'rb') as infile:
        for block in rsa.varblock.yield_fixedblocks(infile, _blocksize):
            count += 1

    infile.close()
    return count


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


if __name__ == '__main__':
    print(count_file_blocks("../file/test.txt"))

