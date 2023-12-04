'''Euler Method

n - количество итераций, h - шаг, (x, y) - начальная точка, x0 = a, x_end = b '''

from math import *

def f(fx, q, w):
    x = q
    y = w
    return eval(fx)

answer = {}
def Euler(fx, n, x0, x_end, y0):
    h = (x_end-x0)/n
    x = x0
    y = y0
    while (x <= x_end-h):
        answer[x] = y
        y += h * f(fx, x, y)
        x += h
    answer[x] = y
    return answer

Euler('y * (1-x)', 10, 0, 1, 1)

