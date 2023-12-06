import math


def quadratic_formula(b, c):
    x1 = (-b - math.sqrt(b**2 - (4 * c))) / 2
    x2 = (-b + math.sqrt(b**2 - (4 * c))) / 2

    return int(x1), int(x2)


x1, x2 = quadratic_formula(71530, 940200)

print(abs(x2 - x1))
