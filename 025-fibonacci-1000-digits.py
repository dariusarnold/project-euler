from math import sqrt, log10
from functools import lru_cache

def int_len(n):
    """
    Get length of integer in digits
    :rtype: int
    """
    return int(log10(n))+1

@lru_cache(maxsize=5000)
def rec_fib(n):
    """
    Calculate nth fibonacci number recursively, use a cache to speed up calculation
    :param n:
    :type n:
    :return:
    :rtype:
    """
    if n == 1: return 1
    if n == 2: return 1
    return rec_fib(n-1) + rec_fib(n-2)

def num_fib(n):
    """
    Calculate nth fibonacci number with a closed form expression
    :param n:
    :type n:
    :return:
    :rtype:
    """
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return ((phi**n - psi**n)/sqrt(5))

def main():
    """
    Calculating fibonacci numbers by closed form expression hits the limit of floating point digits, use
    recursive integer calculation instead, since python integers can become arbitrarily large.
    """
    index = 1
    len = int_len(rec_fib(((index))))
    while (len < 1000):
        index += 1
        len = int_len(rec_fib((index)))
    print(index)

if __name__ == '__main__':
    main()
    print(rec_fib.cache_info())