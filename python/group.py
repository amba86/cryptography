#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://pythoniter.appspot.com/

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


# Return orders of subgroups as list
def order(a):
    l = []
    c = coprime(a)
    cs = len(c)

    for i in range(cs):
        l.append(cs / gcd(cs, i))

    return l


# Return subgroups as dictionary
def subgroup(a):
    d = {}
    l = coprime(a)
    ls = len(l)

    for e in l:
        d[e] = []

        for i in range(ls):
            ee = int((e ** i) % a)

            if 1 == ee and i > 0:
                break

            if ee in l and ee not in d[e]:
                d[e].append(ee)

        # d[e].sort()

    return d


# Returns generators
def generator(a):
    g = []
    c = coprime(a)
    s = subgroup(a)
    cl = len(c)

    for (k, v) in s.iteritems():
        v.sort()

        if len(v) == cl and c == v:
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

