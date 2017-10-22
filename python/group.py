#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://pythoniter.appspot.com/

import math
import json

from fractions import gcd


# Return a list of coprimes
def coprime(a):
    b = a - 1
    l = []

    while b:
        if 1 == gcd(b, a):
            l.append(b)
        b -= 1

    l.sort()

    return l


# Return subgroups as dictionary
def subgroup(a):
    d = {}
    l = coprime(a)
    ls = len(l)

    for e in l:
        d[e] = []

        for i in range(ls):
            ee = math.pow(e, i) % a

            if ee in l:
                if ee not in d[e]:
                    d[e].append(int(ee))

        d[e].sort()

    return d


# Returns generators
def generator(a):
    g = []
    c = coprime(a)
    s = subgroup(a)

    for (k, v) in s.iteritems():
        if c == v:
            g.append(k)

    return g


# Returns length of a content
def l(l):
    return len(l)


# Pretty print specified dictionary
def p(a):
    for (k, v) in a.iteritems():
        v.sort()

    print json.dumps(a, sort_keys=True)

