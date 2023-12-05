import math

a = 0
b = 0.3
h = 0.03
x0 = 2
y0 = 1
z0 = 1
t = a
x, y, z = x0, y0, z0
set_x, set_y, set_z = [], [], []
print('t = ', t, ' ', 'x0 = ', x, ' ', 'y0 = ', y, ' ', 'z0 = ', z)
print('Шаг интегрирования h = ', h)
while t < b - h:
    x = x + h * (-2 * x + 5 * z)
    y = y + h * (math.sin(t - 1) * x - y + 3 * z)
    z = z + h * (-x + 2 * z)
    set_x.append(x)
    set_y.append(y)
    set_z.append(z)
    t += h

for i, j, k in zip(set_x, set_y, set_z):
    print('x = {} \t y = {}\t  z = {}'.format(i, j, k))
