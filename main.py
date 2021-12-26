import os
import math
import sys


def add(a, b):
    import sys
    sys.setrecursionlimit(10000)
    return math.floor(a + b)


def to_sentence(s):
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'


def sub(a, b):
    return math.floor(a - b)

