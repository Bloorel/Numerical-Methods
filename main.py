import numpy as np
import numdifftools as nd

def f(x):
    return 3*pow(x, 4) - 10*pow(x, 3) - pow(x, 2) - 5*x - 3

def метод_хорд(a, b, eps, func):
    похідна_f = nd.Derivative(func, n=1)
    if func(a) * похідна_f(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi - (xi - x0) * func(xi) / (func(xi) - func(x0))
    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - (xi - x0) * func(xi) / (func(xi) - func(x0))
    print('x= ', round(xi_1, 5), ' - Метод хорд')

a1 = -2.0
b1 = -1.0
метод_хорд(a1, b1, 0.0001, f)
