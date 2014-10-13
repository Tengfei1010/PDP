__author__ = 'kevin'
import rsa
import linecache
from common import str2num, gen_indices, gen_coefficients

_blocksize = 512


def gen_proof(pk, chal, challenge_file, tag_file):
    n, g = pk
    c, k1, k2, g_s = chal
    coefficients = []
    p = 1
    for j in range(c):
        str = linecache.getline(tag_file, gen_indices(k1, j))
        t = int(str)
        c = gen_coefficients(k2, j)
        coefficients.append(c)
        p *= pow(t, c)

    sum = 0
    i = 0
    j = 0
    length = len(coefficients)
    with open(challenge_file, 'rb') as infile:
        for block in rsa.varblock.yield_fixedblocks(infile, _blocksize):
            if j == length:
                break
            if i == coefficients[j]:
                result = str2num(_blocksize, block)
                sum += result * coefficients[j]
                j += 1
            i += 1
    return sum, p


if __name__ == '__main__':
    pass
