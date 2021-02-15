from __future__ import print_function, division
import math


def mysqrt(a):
    epsilon = 10 ** (-15)
    x = a / 2
    while True:
        # print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        if abs(y-x) < epsilon:
            break
        x = y
    return x


def test_square_root(a_range):
    for a in a_range:
        my_result = mysqrt(a)
        math_result = math.sqrt(a)
        print('a = ' + str(a))
        print('mysqrt =) ' + str(my_result))
        print('math.sqrt = ' + str(math_result))
        print('diff = ' + str(abs(my_result-math_result)))


def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    epsilon = 10 ** (-15)
    k = 0
    my_pi = 0
    pretag = 2 * math.sqrt(2) / 9801
    while True:
        egesz_resz = factorial(4*k) * (1103 + 26390 * k)
        tort_resz = factorial(k) ** 4 * 396 ** (4*k)
        my_pi += pretag * egesz_resz / tort_resz
        if abs(my_pi - math.pi) < epsilon:
            print(k)
            break
        k += 1


estimate_pi()
