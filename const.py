# right_rectangle
from math import *

x = 0

def f(fx, q):
    x = q
    return eval(fx)


def right_rectangle(fx, a, b, n):
    h = (b - a) / n
    x = a + h
    ans = 0
    while (x <= b):
        ans = ans + f(fx, x)
        x = x + h
    return ans * h


# left_rectangle

def f(fx, q):
    x = q
    return eval(fx)

def left_rectangle(fx, a, b, n):
    h = (b - a) / n
    x = a
    ans = 0
    while (x <= b - h):
        ans = ans + f(fx, x)
        x = x + h
    return ans * h


def left_rectangle_h(fx, a, b, h):
    x = a
    ans = 0
    while (x <= b - h):
        ans = ans + f(fx, x)
        x = x + h
    return ans * h


# parabola

def f(fx, q):
    x = q
    return eval(fx)

def parabola(fx, a, b, n):
    ans = f(fx, a) + f(fx, b)
    h = (b - a) / n
    x = a
    for i in range(n - 1):
        x = x + h
        if (i % 2 != 0):
            ans = ans + 2 * f(fx, x)
        else:
            ans = ans + 4 * f(fx, x)
    return ans * h / 3


#trap

def trap(fx, a, b, n):

    h = (b - a) / n
    s = h * (f(fx, a) + f(fx, b)) * 0.5
    x = a + h

    while (x <= b - h):
        s = s + h * f(fx, x)
        x = x + h
    return s