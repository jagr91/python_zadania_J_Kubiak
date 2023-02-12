# Napisz program, który oblicza przyblizoną wartość liczby e

import math


def e(n):
    s, m = (1.0, 1)
    for i in range(1, n):
        m = m * i
        s = s + 1.0 / m
    return s


print(f'Wartość e z modułu math: {math.e}')
print(f'Wartość e obliczona w programie: {e(20):.15f}')
