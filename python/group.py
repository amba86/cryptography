#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import json

from fractions import gcd

# Return a list of coprimes for a digit
def coprime(a):
    b = a - 1
    l = []

    while b:
        if 1 == gcd(b, a):
            l.append(b)
        b -= 1

    l.sort()

    return l

# Return subgroups of a group specified as list
def subgroup(a):
    d = {}
    l = coprime(a)
    ls = len(l)

    for e in l:
        s = []
        d[e] = s

        for i in range(ls):
            ee = math.pow(e, i) % a

            if ee in l:
                if ee not in s:
                    s.append(int(ee))

    return d

# Pretty print specified content
def p(a):
    for k, v in a.iteritems():
        v.sort()

    print json.dumps(a, sort_keys=True)

