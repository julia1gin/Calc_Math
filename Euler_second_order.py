import matplotlib.pyplot as plt

def euler_second(a, b, h, y, z):
    x = a
    ans = {}
    ans[x] = y
    while x <= b:
        y, z = y+h*z, z - h*(z/x+y)
        x+=h
        ans[x] = y
    return ans


Euler_DE = euler_second(1, 1.5, 0.1, 0.77, -0.44)
x = Euler_DE.keys()
y = Euler_DE.values()

fig, ax = plt.subplots()
plt.title('Метод Эйлера для решения дифференциальных уравнений')
plt.xlabel('x')
plt.ylabel('y')
ax.plot(x, y)
plt.show()
