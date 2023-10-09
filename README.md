#right_rectangle
from math import *

fx = input("Введите функию: ")
a = float(input("Введите нижний предел интегрирования: "))
b = float(input("Введите верхний предел интегрирования: "))
n = int(input("Введите число разбиений: "))

x = 0

def f(func, q):
    x = q
    return eval(fx)

def right_rectangle(fx, a, b, n):
    h = (b - a)/n
    x = a + h
    ans = 0
    while (x <= b):
        ans = ans + f(fx, x)
        x = x + h
    return ans*h

print(right_rectangle(fx,a,b,n))

#left_rectangle
from math import *

fx = input("Введите функию: ")
a = float(input("Введите нижний предел интегрирования: "))
b = float(input("Введите верхний предел интегрирования: "))
n = int(input("Введите число разбиений: "))

x = 0

def f(func, q):
    x = q
    return eval(fx)

def left_rectangle(fx, a, b, n):
    h = (b - a)/n
    x = a
    ans = 0
    while (x <= b - h):
        ans = ans + f(fx, x)
        x = x + h
    return ans*h

print(left_rectangle(fx,a,b,n))

#parabola
from math import *

fx = input("Введите функию: ")
a = float(input("Введите нижний предел интегрирования: "))
b = float(input("Введите верхний предел интегрирования: "))
n = int(input("Введите число разбиений: "))

x = 0

def f(func, q):
    x = q
    return eval(fx)

def parabola(fx, a, b, n):
    ans = f(fx, a) + f(fx, b)
    h = (b - a)/n
    x = a
    for i in range(n-1):
        x = x + h
        if(i%2 != 0):
            ans = ans + 2*f(fx, x)
        else:
            ans = ans + 4*f(fx, x)
    return ans*h/3

print(parabola(fx,a,b,n))



//Метод трапеций// 

from math import *

def trap(a,b,n):
    
    def func(x):
        global formula
        return eval(formula)
    
    h=(b-a)/n
    s=h*(func(a)+func(b))*0.5
    x=a+h
    
    while (x <= b-h):
        s=s+h*func(x)
        x=x+h
    return s

global formula
formula=input("Введите подинтегральную функцию: ")
a=float(input('Введите нижний предел интегрирования: '))
b=float(input('Введите нверхний предел интегрирования: '))
n=int(input('Введите количество разбиений'))
print(trap(a,b,n))

