from math import *

def integral2(f,a,c,b,d,nx,ny):

    def func(fx,q,w):
        x = q
        y = w
        return eval(fx)

    hx=(b-a)/nx
    hy=(d-c)/ny
    x=a
    y=c
    sx=0
    sy=0
    while x<= (b-hx):

        while y<=(d-hy):
            sy=sy+abs(func(f,x,y))
            y=y+hy
        Iy=hy*sy
        sx=sx+Iy
        x=x+hx
        sy=0
        y=c
    Ix=sx*hx
    return(Ix)


