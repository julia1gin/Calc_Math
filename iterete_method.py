from math import *

def f(fx, q, m):
    x = q
    y = m
    return eval(fx)

def iterete_method(fx, x, y, e):
    ef = y
    yx = 0
    while ef > e:
        yx = f(fx, x, y)
        ef = abs(yx-y)
        y = yx
    return yx

