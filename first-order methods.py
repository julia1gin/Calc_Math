# Euler Method for specific function

# n - количество итераций, h - шаг, (x, y) - начальная точка
def Euler(n = 10, a = 0, b = 1):
    h = (b-a)/n
    x = a
    y = b
    while (x <= b-h):
        y += h * function(x, y)
        x += h
    return x, y

def function(x, y):
    return y * (1 - x) # функция первой производной

print(Euler())