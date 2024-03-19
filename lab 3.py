def f(x):
    return x**5 + x**1 - 4

def derivative(func, x, dx=1e-6):
    return (func(x + dx) - func(x)) / dx

def second_derivative(func, x, dx=1e-6):
    return (derivative(func, x + dx) - derivative(func, x)) / dx

def newton_method(a, b, eps, func):
    df = derivative(func, b)
    df2 = second_derivative(func, b)

    if func(b) * df2 > 0:
        xi = b
    else:
        xi = a

    xi_1 = xi - func(xi) / df

    while abs(xi_1 - xi) > eps:
        xi = xi_1
        df = derivative(func, xi)
        xi_1 = xi - func(xi) / df

    print('Метод Ньютона, x = ', round(xi_1, 4))

def combined_method(a, b, eps, func):
    if derivative(func, a) * second_derivative(func, a) > 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a

    ai = a0
    bi = b0

    while abs(ai - bi) > eps:
        ai_1 = ai - func(ai) * (bi - ai) / (func(bi) - func(ai))
        bi_1 = bi - func(bi) / derivative(func, bi)
        ai = ai_1
        bi = bi_1

    x = (ai_1 + bi_1) / 2
    print('Комбінований метод, x = ', round(x, 5))

if __name__ == "__main__":
    a1, b1 = -4, 1
    a2, b2 = 2, 3
    eps = 0.005

    print("Розв'язки на відрізку [-2, -3]")
    newton_method(a1, b1, eps, f)
    combined_method(a1, b1, eps, f)
    print("\nРозв'язки на відрізку [5, 1]")
    newton_method(a2, b2, eps, f)
    combined_method(a2, b2, eps, f)
