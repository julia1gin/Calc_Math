'''Euler Method for specific function

n - количество итераций, h - шаг, (x, y) - начальная точка, x0 = a, x_end = b '''

import matplotlib.pyplot as plt

answer = {}
def Euler(f, n = 10, x0 = 0, x_end = 1, y0 = 1):
    h = (x_end-x0)/n
    x = x0
    y = y0
    while (x <= x_end-h):
        y += h * f(x, y)
        x += h
        answer[x] = y
    return answer

def f(x, y):
    return y * (1 - x) # функция первой производной

Euler_DE = Euler(f)
x = Euler_DE.keys()
y = Euler_DE.values()

fig, ax = plt.subplots()
plt.title('Метод Эйлера для решения дифференциальных уравнений')
plt.xlabel('x')
plt.ylabel('y')
ax.plot(x, y)
plt.show()
