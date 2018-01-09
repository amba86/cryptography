#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://pythoniter.appspot.com/

# Chinese remainder algorithm found on
# http://www.inf.fh-flensburg.de/lang/krypto/algo/chinese-remainder.htm
# c list of coprimes
# r list of remainders
# Returns
# 1. Product of coprimes.
# 2. The chinese remainder.
def cr(c, r):
    if len(c) == 1:
        return (c[0], r[0])
    else:
        j = len(c) // 2
        (m, a) = cr(c[:j], r[:j])
        (n, b) = cr(c[j:], r[j:])
        u = mi(m, n)
        x = u * (b - a) % n * m + a

    return (m * n, x)


# Extended euclidean algorithm
# Returns
# 1. Great common divisor
# 2. Modular inverse of a in ring b
# 3. Modular inverse of b in ring a
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)

    (g, y, x) = egcd(b % a, a)

    return (g, x - b // a * y, y)


# Returns the modular inverse of a % m
# Found on https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def mi(a, m):
    (g, x, y) = egcd(a, m)

    if g != 1:
        return None

    return x % m

