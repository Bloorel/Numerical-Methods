import numpy as np

def f(x):
    return 3*pow(x, 4) - 10*pow(x, 3) - pow(x, 2) - 5*x - 3

def знайти_відрізки(функція, діапазон_пошуку):
    a = None
    previous_x = None
    відрізки = []
    for x in діапазон_пошуку:
        x = round(x, 4)
        поточне_x = функція(x)
        if previous_x is not None and previous_x * поточне_x < 0:
            відрізки.append((a, x))
            a = x
        previous_x = поточне_x
    return відрізки

def метод_половинного_ділення(a, b, eps, функція):
    while abs(a - b) > eps:
        if функція(a) * функція((a + b) / 2) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
    x = (a + b) / 2
    print('x= ', round(x, 5), ' - Метод половинного ділення')

діапазон_пошуку = np.arange(-10, 10, 1)
відрізки = знайти_відрізки(f, діапазон_пошуку)
for a, b in відрізки:
    print(f'Знайдений відрізок: [{a}, {b}]')

for a, b in відрізки:
    метод_половинного_ділення(a, b, 0.0001, f)
