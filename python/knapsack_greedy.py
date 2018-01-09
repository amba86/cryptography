#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://pythoniter.appspot.com/

# Knapsack algorithm

def knapsackGreedy(a, s):
    x = [0] * len(a)
    b = s

    for (i, e) in enumerate(reversed(a)):
        if e > b:
            continue
        else:
            x[len(a) - 1 - i] = 1
            b -= e

    return x

