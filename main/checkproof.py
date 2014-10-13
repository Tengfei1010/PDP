__author__ = 'kevin'
import linecache
from common import gen_coefficients, gen_indices
from common import fast_powmod

_LEAF_FILE = '../file/leaf.txt'


def check_proof(pk, sk, chal, V):
    n, g = pk
    e, v = sk
    c, k1, k2, s = chal
    t, p = V
    t_t = pow(t, e)
    for j in range(c):
        i_j = gen_indices(k1, j)
        a_j = gen_coefficients(k2, j)
        line = linecache.getline(_LEAF_FILE, i_j)
        h_w = int(line)
        t_t = (t_t / (pow(h_w, a_j))) % n
    t_s = fast_powmod(t_t, s, n)
    if t_s == p:
        print("success")
        return "success"
    print("failure")
    return "failure"
