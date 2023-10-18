import math
a = float(input('Введите нижний предел : '))
b = float(input('Введите верхний предел : '))
c=float(input('Введите нижний предел : '))
d=float(input('Введите нижний предел : '))
nx=int(input('число разбиений по х'))
ny=int(input('число разбиений по y'))

def integr2(nx,ny,a,c,b,d):

    def func(x,y):
        return math.sin(x+y)

    hx=(b-a)/nx
    hy=(d-c)/ny
    x=a
    y=c
    sx=0
    sy=0
    while x<= (b-hx):

        while y<=(d-hy):
            sy=sy+abs(func(x,y))
            y=y+hy
        Iy=hy*sy
        sx=sx+Iy
        x=x+hx
        sy=0
        y=c
    Ix=sx*hx
    return(Ix)

print(integr2(nx,ny,a,c,b,d))
