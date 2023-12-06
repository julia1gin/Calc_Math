

def euler_second(a, b, y, z, h):
    x = a
    ans = {}
    ans[x] = y
    while x <= b:
        y, z = y+h*z, z - h*(z/x+y)
        x+=h
        ans[x] = y
    return ans


# Euler_DE = euler_second(1, 1.5, 0.1, 0.77, -0.44)

