#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://pythoniter.appspot.com/

# Chinese remainder algorithm found on
# http://www.inf.fh-flensburg.de/lang/krypto/algo/chinese-remainder.htm
def cr(nn, rr):
    if len(nn) == 1:
        return (nn[0], rr[0])
    else:
        j = len(nn) // 2
        (m, a) = chineseRemainder(nn[:j], rr[:j])
        (n, b) = chineseRemainder(nn[j:], rr[j:])
        u = modinverse(m, n)
        x = u * (b - a) % n * m + a
    return (m * n, x)

