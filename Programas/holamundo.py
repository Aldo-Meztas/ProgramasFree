import numpy as np
import matplotlib.pyplot as plt
import math
# import PyQt5

def triangular(x, a, b, c):
    rT = []
    for i in x:
        if i <= a:
            rT.append(0)
        elif a <= i and i <= b:
            rT.append((i-a)/(b-a))
        elif b <= i and i <= c:
            rT.append((c-i)/(c-b))
        elif c <= i:
            rT.append(0)
        else:
            pass
    return np.array(rT)


def trapezoidal(x, a, b, c, d):
    rT = []
    for i in x:
        if i <= a:
            rT.append(0)
        elif a <= i and i <= b:
            rT.append((i-a)/(b-a))
        elif b <= i and i <= c:
            rT.append(1)
        elif c <= i and i <= d:
            rT.append((d-i)/(d-c))
        elif d <= i:
            rT.append(0)
    return np.array(rT)


def gausseana(x, a, b):
    e = math.e
    return e**((-(1/2))*((x-a)/b)**2)


def campana(x, a, b, c):
    return 1/(1+(abs((x-c)/a))**(2*b))


def rangos(inicio, final):
    return np.array([float(i) for i in range(inicio, final+1)])


def entrada():
    print("========== INGRESE RANGO ==========")
    inicio = int(input("Ingrese inicio: "))
    final = int(input("Ingrese final: "))
    print("===================================")
    return rangos(inicio, final)

print("Triangular")
x = entrada()
valor1 = triangular(x, 6, 7, 9)
xt = x
yt = valor1
plt.plot(xt, yt, 'b--', label="Triangular")

print("Trapezoidal")
x = entrada()
valor2 = trapezoidal(x, 5, 6, 8, 10)
xtr = x
ytr = valor2
plt.plot(xtr, ytr, 'r--', label="Trepecio")

print("Gausiana")
x = entrada()
valor3 = gausseana(x, 3, 0.7)
xg = x
yg = valor3
plt.plot(xg, yg, label="Gausiana")

print("Campana")
x = entrada()
valor4 = campana(x, 1.5, 5, 3)
xc = x
yc = valor4
plt.plot(xc, yc, label="Campana")
plt.legend(loc='upper left')
plt.show()
