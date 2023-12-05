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
