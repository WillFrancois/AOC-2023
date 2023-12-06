import math


def quadratic_formula(b, c):
    x1 = (-b - math.sqrt(b**2 - (4 * c))) / 2
    x2 = (-b + math.sqrt(b**2 - (4 * c))) / 2

    print(x1, x2)


print(quadratic_formula(71530, 940200))
