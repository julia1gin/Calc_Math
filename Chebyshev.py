def e_in_degree_x(x, accuracy):
    arr = [0.99999998, 1, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
    c = arr[0]
    p = 1
    k = 1
    u = 100
    while abs(u) > accuracy:
        p *= x
        u = p*arr[k]
        c += u
        k +=1
        if k == len(arr):
            break
    return c

def sin_in_degree_x(x, accuracy):
    arr = [1.0000000002, -0.1666666589, 0.008333075, -0.000198107, 0.000002608]
    c = 0
    k = 0
    u = 100
    if x == 0:
        c = 0
        return c
    else:
        p = 1/x
    while abs(u) > accuracy:
        p *= x*x
        u = p*arr[k]
        c += u
        k += 1
        if k == len(arr):
            break
    return c